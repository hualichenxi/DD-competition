#! /usr/bin/python
import numpy
import datetime
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor

def loadColumns(s):
	f = open(s)
	lines = f.readlines()
	f.close()
	a = []
	for line in lines:
		line = line.replace('\\N','0')
		a.append([float(i) for i in line.strip().split(' \x01')])
	return numpy.array(a)

# fs = ['gap1','gap2','gap3','ifmpeak','ifepeak','iffestival','ifweekday','dayofweek','dayofweekday']

fs = ['gap1','gap2','gap3','gap_average','gap_latest']


print 'load data...\n'
tr_y = loadColumns('../data/train_y/000000_0')
tr_x = numpy.empty([tr_y.shape[0],0])
for f in fs:
	tr = loadColumns('../data/train_x_'+f+'/000000_0')
	print f
	print tr.shape
	tr_x = numpy.concatenate((tr_x,tr),axis=1)


cv = cross_validation.ShuffleSplit(tr_y.shape[0], n_iter=3, test_size=0.2,random_state=0)

print "岭回归"
starttime = datetime.datetime.now()    
for train, test in cv:    
    svc = linear_model.Ridge().fit(tr_x[train], tr_y[train,2])
    print("train score: {0:.3f}, test score: {1:.3f}\n".format(svc.score(tr_x[train], tr_y[train,2]), svc.score(tr_x[test], tr_y[test,2])))
endtime1 = datetime.datetime.now()
print str((endtime1 - starttime).seconds) + ' seconds used.\n'
    
print "线性回归"    
for train, test in cv:    
    regr = linear_model.LinearRegression().fit(tr_x[train], tr_y[train,2])
    print("train score: {0:.3f}, test score: {1:.3f}\n".format(regr.score(tr_x[train], tr_y[train,2]), regr.score(tr_x[test], tr_y[test,2])))
joblib.dump(regr, "model/model.m")
endtime2 = datetime.datetime.now()
print str((endtime2 - endtime1).seconds) + ' seconds used.\n'
 
# print "支持向量回归/SVR(kernel='rbf',C=10,gamma=.001)"
# for train, test in cv:
#     svc = svm.SVR(kernel ='rbf', C = 10, gamma = .001).fit(tr_x[train], tr_y[train,2])
#     print("train score: {0:.3f}, test score: {1:.3f}\n".format(
#         svc.score(tr_x[train], tr_y[train,2]), svc.score(tr_x[test], tr_y[test,2])))
# endtime3 = datetime.datetime.now()
# print str((endtime3 - endtime2).seconds) + ' seconds used.\n'
 
print "随机森林回归/Random Forest(n_estimators = 5)"    
for train, test in cv:    
    svc = RandomForestRegressor(n_estimators = 5).fit(tr_x[train], tr_y[train,2])
    print("train score: {0:.3f}, test score: {1:.3f}\n".format(svc.score(tr_x[train], tr_y[train,2]), svc.score(tr_x[test], tr_y[test,2])))
endtime4 = datetime.datetime.now()
print str((endtime4 - endtime2).seconds) + ' seconds used.\n'
 

# starttime = datetime.datetime.now()
# regr = linear_model.LinearRegression()
# regr.fit(tr_x,tr_y[:,2])
# joblib.dump(regr, "model/model.m")

# endtime1 = datetime.datetime.now()
# print str((endtime1 - starttime).seconds) + ' seconds used.\n'


