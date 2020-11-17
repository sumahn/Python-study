#!/usr/bin/env python
# coding: utf-8

# In[3]:


import warnings
from abc import *
import catboost
import lightgbm as lgb
from bayes_opt import BayesianOptimization
from metrics import mape_transform, CatBoostMapeExp
from utils import *
from matplotlib.font_manager import fontManager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.linear_model import LinearRegression, Lasso, Ridge
# import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Malgun Gothic'
sns.set(font='Malgun Gothic',
       rc ={'axes.unicode_minus':False},
       style='whitegrid')

        

warnings.filterwarnings("ignore", category=UserWarning)

class BoosterBase(metaclass=ABCMeta):

    def __init__(self, params):
        self.params = params
        self.optimizer = None

    @abstractmethod
    def train(self, trainset, testset, params, verbose_eval):
        pass

    @abstractmethod
    def get_best(self, model):
        pass

    def optimize(self, data, pbounds, init_points, n_iter, interval=0, isnull=False):
        def objective(**kwargs):
            integer_params = ['num_leaves', 'max_depth','min_data_in_leaf','max_bin',
                             'iterations','depth','max_leaves','border_count']
        
            for key,value in pbounds.items():
                if key in integer_params:
                    kwargs[key] = int(kwargs[key])
                else:
                    kwargs[key] = kwargs[key]
            params = dict(self.params, **kwargs)
           

            if isnull:
                null_score = self.tsCV(data, interval, params, null_modeling=True)
                return -1 * null_score

            _, normal_score, _, _ = self.tsCV(data, interval, params)
            return -1 * normal_score
        if self.optimizer is None:
            self.optimizer = BayesianOptimization(objective, pbounds, random_state=2020)
        else:
            self.optimizer.set_bounds(pbounds)
        self.optimizer.maximize(init_points=init_points, n_iter=n_iter)
        self.params = dict(self.params, **self.optimizer.max['params'])



    def tsCV(self, data, interval, params=None, verbose=False, verbose_plot=False, isnormal=False, isnull=False,
             null_modeling=False):
        """
        시계열 교차검증 결과 반환
        :param data: 판다스 데이터프레임 or 파일명 문자열
        :param interval: 타겟 월로부터 몇 개월 전까지의 데이터를 사용할지
        :param params: 부스터 파라미터
        :param verbose: cv 과정 출력 여부
        :return: 월별 F1 스코어 평균, 반복 횟수
        """

        data = get_data(data)

        data.rename(columns={"월":"month"}, inplace=True)
        normal_scores = []
        normal_iters = []
        null_scores = []
        null_iters = []
        scores = []
        target_month_list = []
        normal_result = {}
        null_result = {}

        row_format = "{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}"
        if verbose:
            print(row_format.format("target month", "mape", "normal mape", "null mape", "normal iters", "null iters"))
            print(row_format.format("=" * 15, "=" * 15, "=" * 15, "=" * 15, "=" * 15, "=" * 15))
        min_month = data.month.min()
        max_month = data.month.max()
        
        
        # target month 올려가면서 검증
        for target_month in range(min_month + 1, max_month + 1):
            if interval == 0:
                # interval == 0 인 경우 활용 가능한 모든 데이터 학습
                start_month = min_month
            else:
                # 그 외의 경우 interval 만큼만 학습
                start_month = target_month - interval
                if start_month < min_month:
                    continue
            
            target_month_list.append(target_month)
            trainset, testset = ts_split(data, start_month, target_month)

#             trainset, testset = encode_categorical_features(trainset, testset,cat_vars)
            
            normal = testset[testset.상품명.isin(trainset.상품명)]
            null = testset[~testset.상품명.isin(trainset.상품명)]
            n_normal = normal.shape[0]
            n_null = null.shape[0]

            normal_model = self.train(trainset, normal, params, verbose_eval=False)
            normal_pred = self.predict(normal_model, normal)
            normal_result[target_month] = normal_pred
         
            normal_score, normal_iter = self.get_best(normal_model)
            normal_score = round(normal_score, 4)
            normal_scores.append(normal_score)
            normal_iters.append(normal_iter)

            null_model = self.train(trainset, null, params, verbose_eval=False)
            null_pred = self.predict(null_model, null)
            null_result[target_month] = null_pred
            null_score, null_iter = self.get_best(null_model)
            null_score = round(null_score, 4)
            null_scores.append(null_score)
            null_iters.append(null_iter)

            score = round((normal_score * n_normal + null_score * n_null)/(n_normal + n_null), 4)
            scores.append(score)

            
            if verbose:
                print(row_format.format(target_month, score, normal_score, null_score, normal_iter, null_iter))

        score = round(np.mean(scores), 4)
        normal_score = round(np.mean(normal_scores), 4)
        null_score = round(np.mean(null_scores), 4)
        normal_iter = round(np.mean(normal_iters))
        null_iter = round(np.mean(null_iters))


        if verbose:
            print(row_format.format("=" * 15, "=" * 15, "=" * 15, "=" * 15, "=" * 15, "=" * 15))
            print(row_format.format("mean", score, normal_score, null_score, normal_iter, null_iter))
            
            
        if verbose_plot:
            df = pd.DataFrame(index=target_month_list, data={
                              'normal_mape': normal_scores,
                              'null_mape':null_scores,
                              'scores':scores})
            
            fig = plt.figure(figsize=(12,6))
            ax = fig.add_subplot()
            normal_mape_plot, =ax.plot(df.index, df['normal_mape'], 'r', label="normal_mape")
            null_mape_plot, = ax.plot(df.index, df['null_mape'], 'b', label="null_mape")
            score_plot, = ax.plot(df.index, df['scores'], 'g', label="total_mape")
            plt.xlabel("Target month")
            plt.ylabel("MAPE")
            plt.title("tsCV result")
            leg = ax.legend([normal_mape_plot, null_mape_plot, score_plot], ["normal_mape","null_mape","total_mape"],loc="upper right")
            ax.add_artist(leg)
            
            
        if isnormal:
            return normal_result
        
        
        if isnull:
            return null_result


        if null_modeling:
            return null_score


        return score, normal_score, normal_iter, null_iter
    

    def feature_impo(self, data, target_month, params, isnull=False, isnormal=False,
                     ax=None, importance_type="split", title="Feature ipmortance",
                     xlabel = "Feature importance", ylabel="Features", height=0.2,
                     xlim=None, ylim=None,
                     max_num_features=None, figsize=None, grid=True, precision=None,
                     **kwargs):
        data = data.rename(columns={"월":"month"})

        # model = self.train(trainset, testset, params, verbose_eval=False)
        feature_name = data.columns.tolist()

        if isnull:
            cat_vars = ['마더코드', '상품코드', '상품명', '상품군', '공휴일여부', '브랜드', 'NS상품군_대', 'NS상품군_중', 'NS상품군_소', 'prodnames',
                        '성별',
                        '결제방법', '세트여부', 'cluster', '일', '시간', '분', '요일', '계절', ]
            data[cat_vars] = data[cat_vars].fillna("NA").astype(dict(zip(cat_vars, ["category" for _ in cat_vars])))
            data = data.assign(**{feature: LabelEncoder().fit_transform(data[feature].astype(str)) for feature in cat_vars})

            trainset = data.loc[lambda x: x.month < target_month]
            testset = data.loc[lambda x: x.month == target_month]

            null_test = testset[~testset.상품명.isin(trainset.상품명)]
            null_model = self.train(trainset, null_test, params, verbose_eval =False)
            importance = null_model.feature_importance(importance_type = importance_type)

        if isnormal:
            trainset = data.loc[lambda x: x.month < target_month]
            testset = data.loc[lambda x: x.month == target_month]

            normal_test = testset[testset.상품명.isin(trainset.상품명)]
            normal_model = self.train(trainset, normal_test, params, verbose_eval=False)
            importance = np.round(normal_model.feature_importances_, 4)

        if not len(importance):
            raise ValueError("Booster's feature_importance is empty.")

        tuples = sorted(zip(feature_name, importance), key=lambda x:x[1])

        if max_num_features is not None and max_num_features > 0:
            tuples = tuples[-max_num_features:]

        labels, values = zip(*tuples)

        if ax is None:
            if figsize is not None:
                check_not_tuple_of_2_elements(figsize, 'figsize')
            _, ax = plt.subplots(1, 1, figsize=figsize)

        ylocs = np.arange(len(values))
        ax.barh(ylocs, values, align='center', height=height, **kwargs)

        for x, y in zip(values, ylocs):
            ax.text(x + 1, y,
                    _float2str(x, precision) if importance_type == 'gain' else x,
                    va='center')

        ax.set_yticks(ylocs)
        ax.set_yticklabels(labels)

        if xlim is not None:
            check_not_tuple_of_2_elements(xlim, 'xlim')
        else:
            xlim = (0, max(values) * 1.1)
        ax.set_xlim(xlim)

        if ylim is not None:
            check_not_tuple_of_2_elements(ylim, 'ylim')
        else:
            ylim = (-1, len(values))
        ax.set_ylim(ylim)

        if title is not None:
            ax.set_title(title)
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        ax.grid(grid)
        return ax

        # return lgb.plot_importance(null_model, max_num_features=10, figsize=(16,10))

         # return lgb.plot_importance(normal_model, max_num_features=10, figsize=(16,10))

        # return lgb.plot_importance(model, max_num_features=10, figsize=(16,10))
        

    def backward(self, data, interval):
        backward_scores = []
        features = list(set(data.columns) - {"target", "month"})
        for feature in features:
            score, _, _ = self.tsCV(data.drop(feature, axis=1), interval)
            backward_scores.append(score)
        best_score = np.min(backward_scores)
        drop_feature = features[backward_scores.index(best_score)]
        return best_score, drop_feature

    def backward_selection(self, data, interval, params):
        """
        tsCV 결과를 통해 백워드 방식으로 변수 선택
        :param data: 판다스 데이터프레임 / 파일명 문자열
        :param interval:
        :return: 제거된 변수들의 리스트 반환
        """
        data = get_data(data)
        dropped_features = []
        current_score, _, _ = self.tsCV(data, interval, params)
        while data.shape[1] > 3:
            backward_score, drop_feature = self.backward(data, interval)
            if current_score >= backward_score:
                print(f"Score: {backward_score}   Drop: {drop_feature}")
                data = data.drop(drop_feature, axis=1)
                dropped_features.append(drop_feature)
                current_score = backward_score
            else:
                break
        print("Dropped features:", dropped_features)
        return dropped_features



class LightGBM(BoosterBase):
    def __init__(self, params=None):
        super().__init__(params)
        if params is None:
            self.params = dict(
#                 learning_rate=0.2,
                objective="regression",
                metric="custom",
                verbosity=-1
            )
        self.create_dataset = lightgbm_dataset

    def train(self, trainset, testset, params, verbose_eval=False):
        if params is None:
            params = self.params
        trainset = self.create_dataset(trainset)
        testset = self.create_dataset(testset)
        test_result = {}
        model = lgb.train(
            params=params,
            train_set=trainset,
            valid_sets=testset,
            num_boost_round=1000,
            verbose_eval=verbose_eval,
            feval=mape_transform,
            early_stopping_rounds=100,
            evals_result=test_result
        )

        return model
    
    
    
        

    def get_best(self, model):
        score = model.best_score["valid_0"]["mape_exp"]
        iteration = model.best_iteration
        return round(score, 4), iteration
    
    
    def predict(self, model, testset):
        y_pred = model.predict(testset)
        log_result = testset.assign(log_pred = y_pred)
        result = testset.assign(pred = np.exp(y_pred))
        return result


    def make_result(self, data, params, n_iter):

        # data 불러오기
        data = pd.read_csv('../data/train/data.csv')

        origin_test = pd.read_excel('../data/test/test.xlsx', header=1)

        merged_data = pd.merge(origin_test[["방송일시","상품코드","상품명"]].astype(dict(방송일시=str)), data[data["취급액"].isna()],
                 how="left")

        data = pd.concat([data[~data.취급액.isna()], merged_data])
        data = data.assign(로그_취급액 = np.log(data.취급액)).drop(columns=["취급액","방송일시"])

        data.rename(columns = {"월":"month"}, inplace=True)
        cat_vars = ['마더코드', '상품코드', '상품명', '상품군', '공휴일여부', '브랜드', 'NS상품군_대', 'NS상품군_중', 'NS상품군_소', 'prodnames', '성별',
                    '결제방법', '세트여부', 'cluster', '일', '시간', '분', '요일', '계절', ]
        data[cat_vars] = data[cat_vars].fillna("NA").astype(dict(zip(cat_vars, ["category" for _ in cat_vars])))
        data = data.assign(**{feature: LabelEncoder().fit_transform(data[feature].astype(str)) for feature in cat_vars})

        trainset = data.loc[lambda x:x.로그_취급액.isnull() == False]
        testset = data.loc[lambda x:x.로그_취급액.isnull() == True]
        # normal, null 분할

        normal = testset[testset.상품명.isin(trainset.상품명)]
        null = testset[~testset.상품명.isin(trainset.상품명)]

        trainset = self.create_dataset(trainset)
        testset = self.create_dataset(testset)

        model = lgb.train(
            params = params,
            train_set = trainset,
            num_boost_round = n_iter
        )
        pred = self.predict(model, null)

        return model,pred


class CatBoost(BoosterBase):
    def __init__(self, params=None):
        super().__init__(params)
        if params is None:
            self.params = dict(
                loss_function="RMSE",
                eval_metric=CatBoostMapeExp(),
                 learning_rate=0.1
            )
        self.create_dataset = catboost_dataset

    def train(self, trainset, testset, params, verbose_eval=False):
        if params is None:
            params = self.params
        trainset = self.create_dataset(trainset)
        testset = self.create_dataset(testset)
        model = catboost.train(
            pool=trainset,
            params=params,
            verbose=verbose_eval,
           iterations=3000,
            eval_set=testset,
            early_stopping_rounds=100
        )
        return model

    def get_best(self, model):
        score = model.get_best_score()["validation"]["CatBoostMapeExp"]
        iteration = model.get_best_iteration()
        return round(score, 4), iteration
    
    
    def predict(self, model, testset):
        y_pred = model.predict(testset)
        log_result = testset.assign(log_pred = y_pred)
        result = testset.assign(pred = np.exp(y_pred))
        return result

    def make_result(self, data, params, n_iter):

        # data 불러오기
        data = pd.read_csv('../data/train/data.csv')
        origin_test = pd.read_excel('../data/test/test.xlsx', header=1)
        merged_test = pd.merge(origin_test.astype(dict(방송일시=str)), data[data["취급액"].isna()],
                               how="left")
        data = pd.concat([data[~data.취급액.isna()], merged_test])
        data = data.assign(로그_취급액=np.log(data.취급액)).drop(columns=["취급액", "방송일시"])
        data.rename(columns = {"월":"month"}, inplace=True)

        cat_vars = ['마더코드', '상품코드', '상품명', '상품군', '공휴일여부', '브랜드', 'NS상품군_대', 'NS상품군_중', 'NS상품군_소', 'prodnames', '성별',
                    '결제방법', '세트여부', 'cluster', '일', '시간', '분', '요일', '계절', ]

        data[cat_vars] = data[cat_vars].fillna("NA").astype(str).astype(dict(zip(cat_vars, ["category" for _ in cat_vars])))

        trainset = data.loc[lambda x:x.로그_취급액.isnull() == False]
        testset = data.loc[lambda x:x.로그_취급액.isnull() == True]

        # normal, null 분할
        normal = testset[testset.상품명.isin(trainset.상품명)]
        null = testset[~testset.상품명.isin(trainset.상품명)]

        trainset = self.create_dataset(trainset)

        model = catboost.train(
            pool = trainset,
            params= params,
            iterations = n_iter,
            verbose=False
        )

        pred = self.predict(model, normal)


        return model, pred

# In[ ]:




