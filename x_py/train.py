#coding=utf-8
import pandas as pd 
import numpy as np 
from pandas import Series,DataFrame
import datetime
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.learning_curve import learning_curve
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import explained_variance_score



fs = ['gap1','gap2','gap3','ifmpeak','ifepeak','iffestival','ifweekday','dayofweek','dayofweekday']
#fs = ['gap1']
print 'load data...\n'

train_pd = pd.read_csv('../data/train_y/000000_0', names=['id','district_id','gap'], sep=' ', dtype={'id':object,'district_id':object,'gap':object})

for f in fs:
	tmp = pd.Series.from_csv('../data/train_x_'+f+'/000000_0', index_col=False)
	train_pd[f]=tmp
	train_pd.loc[(train_pd[f].astype(str)=='\N'),f]=0
	print f
print train_pd.info()
#train_pd.head()

df_train_target=train_pd['gap'].astype(int).values
df_train_data=train_pd.drop(['id','district_id','gap'],axis=1).values

print 'feature shape is ', df_train_data.shape
print 'target shape is ', df_train_target.shape


cv = cross_validation.ShuffleSplit(len(df_train_data), n_iter=3, test_size=0.2,random_state=0)

print "随机森林回归/Random Forest(n_estimators = 100)"    
for train, test in cv:    
    svc = RandomForestRegressor(n_estimators = 100).fit(df_train_data[train], df_train_target[train])
    print("train score: {0:.3f}, test score: {1:.3f}\n".format(svc.score(df_train_data[train], df_train_target[train]), svc.score(df_train_data[test], df_train_target[test])))









