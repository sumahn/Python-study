#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def mape(true, pred): 
    return np.mean(np.abs((true - pred) / true))


def mape_transform(preds, train_data, inverse_transform=np.exp):
    """
    - lightgbm 평가용 함수
    - y의 역변환에 대한 mape를 반환(default=exp)
    """
    labels = train_data.get_label()
    score = mape(inverse_transform(labels), inverse_transform(preds))
    return 'mape_exp', score, False


class CatBoostMapeExp(object):

    def get_final_error(self, error, weight):
        return error

    def is_max_optimal(self):
        return False

    def evaluate(self, approxes, target, weight):
        # approxes - list of list-like objects (one object per approx dimension)
        # target - list-like object
        # weight - list-like object, can be None
        assert len(approxes) == 1
        assert len(target) == len(approxes[0])

        target = np.exp(target)
        approx = np.exp(approxes[0])
        score = mape(target, approx)

        return score, 1


# In[ ]:




