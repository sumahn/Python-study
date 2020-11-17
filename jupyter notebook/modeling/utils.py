#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pickle
import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from lightgbm import Dataset
from catboost import Pool
from pandas import CategoricalDtype
from fuzzywuzzy import fuzz, process
import warnings
warnings.filterwarnings(action='ignore')


def read_pickle(fname):
    with open(fname, "rb") as picklefile:
        obj = pickle.load(picklefile)
    return obj


def save_pickle(fname, obj):
    with open(fname, "wb") as picklefile:
        pickle.dump(obj, picklefile)
    print(f"Saved pickle: {fname}")


def catboost_dataset(data, dep_var="로그_취급액"):
    data.dropna(inplace=True)
    x, y = data.drop(columns=[dep_var]), data[dep_var]
    cat_vars = ['마더코드', '상품코드', '상품명', '상품군', '공휴일여부', '브랜드', 'NS상품군_대', 'NS상품군_중', 'NS상품군_소', 'prodnames', '성별', '결제방법', '세트여부', 'cluster', '일', '시간', '분', '요일', '계절']
    return Pool(data=x, label=y, cat_features=cat_vars)


def lightgbm_dataset(data, dep_var="로그_취급액"):
    x, y = data.drop(columns=[dep_var]), data[dep_var]
    cat_vars = [idx for idx, val in enumerate(data.dtypes) if isinstance(val, CategoricalDtype)]
    return Dataset(x.values, y.values, free_raw_data=False, categorical_feature=cat_vars)


def target_encode(train, test, cols, dep_var="로그_취급액"):
    encoder = TargetEncoder(cols=cols, drop_invariant=False, min_samples_leaf=10)
    encoder.fit(train, train[dep_var])
    return encoder.transform(train), encoder.transform(test)


def split_dataset(data, train_index, test_index):
    return data.iloc[train_index], data.iloc[test_index]


def get_data(data):
    if type(data) == str:
        data = pd.read_csv(f"../data/train/{data}")
    else:
        assert isinstance(data, pd.DataFrame)
    if "로그_취급액" not in data.columns:
        data = data.assign(로그_취급액=np.log(data.취급액)).drop("취급액", axis=1)
    dropcols = ["방송일시", "방송종료", "test"]
    data = data.drop(columns=dropcols, errors='ignore')
    return data


def ts_split(data, start_month, target_month):
    trainset = data[(data.month.astype(int) < target_month) & (data.month.astype(int) >= start_month)]
    testset = data[data.month.astype(int) == target_month]
    return trainset, testset


def impute(trainset, testset):
    # impute prodnames
    trainset = trainset.drop_duplicates("상품명")
    train_prodnames = trainset.상품명
    test_prodnames = testset[~testset.상품명.isin(trainset.상품명)].상품명.astype(str).unique()
    imputation = {prodname: process.extractOne(prodname, train_prodnames, scorer=fuzz.token_sort_ratio)[0] for
                  prodname in test_prodnames}
    testset = testset.assign(상품명=testset.상품명.replace(imputation))
    assert trainset.상품명.isin(trainset.상품명).all()
    # impute mothercodes
    testset = testset.drop("마더코드", axis=1).reset_index().merge(trainset[["상품명", "마더코드"]], how="left").set_index(
        'index')
    assert trainset.마더코드.isin(trainset.마더코드).all()
    return testset[trainset.columns.to_list() + ["is_normal"]]


def encode_categorical_features(trainset, testset, cat_vars):
    for feature in cat_vars:
        encoder = {val: idx for idx, val in enumerate(trainset[feature].drop_duplicates().sort_index().values)}
        testset[feature] = [int(encoder.get(x)) if x in trainset[feature].values else -1 for x in
                            testset[feature]]
        trainset[feature] = trainset[feature].map(encoder).astype(int)
    trainset = trainset.astype(dict(zip(cat_vars, ["category" for _ in cat_vars])))
    testset = testset.astype(dict(zip(cat_vars, ["category" for _ in cat_vars])))
    return trainset, testset

def check_not_tuple_of_2_elements(obj, obj_name='obj'):
    """Check object is not tuple or does not have 2 elements."""
    if not isinstance(obj, tuple) or len(obj) != 2:
        raise TypeError('%s must be a tuple of 2 elements.' % obj_name)

def _float2str(value, precision=None):
    return ("{0:.{1}f}".format(value, precision)
            if precision is not None and not isinstance(value, string_type)
            else str(value))

def make_submission(null_result, normal_result):
    test = pd.read_excel('../data/test/test.xlsx', header=1)
    result = pd.concat([null_result, normal_result])
    result.rename(columns={"month":"월"}, inplace=True)

    sub = pd.merge(test, result[["pred"]], left_index=True, right_index=True)
    sub.rename(columns = {"pred":"예상취급액"}, inplace=True)
    sub.drop(columns=["취급액"], inplace=True)
    sub["예상취급액"] = np.where(sub["상품군"] != "무형", sub["예상취급액"], np.nan)
    print(sub.shape)
    return sub

# In[ ]:




