#!/usr/bin/env python
# coding: utf-8

# In[24]:


import sys
#sys.path.append("..")
import fire
import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, train_test_split
from metrics import mape_transform
from utils import target_encode, lgbm_dataset, split_dataset
import warnings


# In[25]:


warnings.filterwarnings("ignore")


# In[26]:


params = dict(objective="regression",
             metric = "custom",
             learning_rate = 0.1,
             verbosity=1)


# In[27]:


def get_score(train, test, verbose_eval=False, params=params):
    test_result = {}
    model = lgb.train(params = params,
                     train_set = train,
                     valid_sets = test,
                     num_boost_round = 3000,
                     feval = mape_transform,
                     early_stopping_rounds = 100,
                     evals_result = test_result,
                     verbose_eval = verbose_eval)
    return min(test_result["valid_0"]["mape_exp"])


# In[32]:


class TargetEncodingCV:
    def __init__(self):
        pass
    
    def run(self, data, encoding_cols, dep_vars="로그_취급액",n_splits=5):
        print("Reading Data ...")
        if "/" not in data:
            data = f"../data/train/{data}"
        data = pd.read_csv(data)
        
        validationScores = []
        kfold = KFold(n_splits, random_state=2020)
        cv_dataset, test_dataset = train_test_split(data, test_size=0.2, random_state=2020)
        i = 0
        print("Cross Validation...")
        for train_index, valid_index in kfold.split(cv_dataset):
            train, valid = split_dataset(cv_dataset, train_index, valid_index)
            train, valid = target_encode(train, valid, encoding_cols, dep_var =dep_var)
            cat_vars = list(set(train.columns[data.dtypes=="category"].values) - set(encoding_cols))
            train, valid = lgb_dataset(train, cat_vars, dep_var=dep_var), lgb_dataset(valid, cat_vars, dep_var=dep_var)
            score = get_score(train, valid)
            print(f"{i + 1}th fold: {score}")
            validationScores.append(score)
            i += 1
        
        validationScores = np.array(validationScores)
        mape_mean, mape_std = validationScores.mean().round(4), validationScores.std().round(4)
        print(f"CV MAPE MEAN: {mape_mean} ± {mape_std}(std)")

        train, test = target_encode(cv_dataset, test_dataset, encoding_cols, dep_var=dep_var)
        train, valid = lgb_dataset(train, cat_vars, dep_var=dep_var), lgb_dataset(test, cat_vars, dep_var=dep_var)
        score = get_score(train, valid, verbose_eval=100)
        print(f"TEST MAPE: {score}")
    
    if __name__=="__main__":
        fire.Fire(TargetEncodingCV)
        


# In[42]:


import sys
sys.path.append("..")
import fire
import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, train_test_split
from metrics import mape_transform
from utils import target_encode, lgbm_dataset, split_dataset
import warnings

warnings.filterwarnings("ignore")

params = dict(
    objective='regression',
    metric="custom",
    learning_rate = 0.1,
    # first_metric_only = False,
    verbosity=-1
)


def get_score(train, test, verbose_eval=False, params=params):
    test_result = {}
    model = lgb.train(
        params=params,
        train_set=train,
        valid_sets=test,
        num_boost_round=3000,
        feval=mape_transform,
        early_stopping_rounds=100,
        evals_result=test_result,
        verbose_eval=verbose_eval
    )
    return min(test_result["valid_0"]["mape_exp"])


class TargetEncodingCV:
    def __init__(self):
        pass

    def run(self, data, encoding_cols, dep_var="로그_취급액", n_splits=5):
        print("Reading Data ...")
        if "/" not in data:
            data = "../data/train/{}".format(data)
        data = pd.read_csv(data)

        validationScores = []
        kfold = KFold(n_splits, random_state=2020)
        cv_dataset, test_dataset = train_test_split(data, test_size=0.2, random_state=2020)
        i = 0
        print("Cross Validation ...")
        for train_index, valid_index in kfold.split(cv_dataset):
            train, valid = split_dataset(cv_dataset, train_index, valid_index)
            train, valid = target_encode(train, valid, encoding_cols, dep_var=dep_var)
            cat_vars = list(set(train.columns[data.dtypes == "category"].values) - set(encoding_cols))
            train, valid = lgb_dataset(train, cat_vars, dep_var=dep_var), lgb_dataset(valid, cat_vars, dep_var=dep_var)
            score = get_score(train, valid)
            print("{i + 1}th fold: {}".format(score))
            validationScores.append(score)
            i += 1
        validationScores = np.array(validationScores)
        mape_mean, mape_std = validationScores.mean().round(4), validationScores.std().round(4)
        print(f"CV MAPE MEAN: {mape_mean} ± {mape_std}(std)")

        train, test = target_encode(cv_dataset, test_dataset, encoding_cols, dep_var=dep_var)
        train, valid = lgbm_dataset(train, cat_vars, dep_var=dep_var), lgbm_dataset(test, cat_vars, dep_var=dep_var)
        score = get_score(train, valid, verbose_eval=100)
        print(f"TEST MAPE: {score}")

        
    if __name__== "__main__":
        TargetEncodingCV


# In[ ]:




