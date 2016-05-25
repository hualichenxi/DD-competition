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

fs = ['gap1','gap2','gap3','ifmpeak','ifepeak','iffestival','ifweekday','dayofweek','dayofweekday']

print 'load data...\n'
tr_y = loadColumns('../data/train_y/000000_0')
y_min,y_max = min(tr_y[:,2]),max(tr_y[:,2])
tr_y[:,2]=(tr_y[:,2]-y_min)/(y_max-y_min)
print 'y_min: ' + str(y_min) + '  y_max: ' + str(y_max)

tr_x = numpy.empty([tr_y.shape[0],0])
for f in fs:
	print f
	tr = loadColumns('../data/train_x_'+f+'/000000_0')
	tr_min,tr_max = min(tr[:,0]),max(tr[:,0])
	tr[:,0] = (tr[:,0]-tr_min)/(tr_max-tr_min)
	tr_x = numpy.concatenate((tr_x,tr),axis=1)

print 'sample #: ' + str(tr_y.shape[0]) 

cv = cross_validation.ShuffleSplit(tr_y.shape[0], n_iter=3, test_size=0.2,random_state=0)

print "linear mode Ridge"
starttime = datetime.datetime.now()    
tr_score,te_score=0.0,0.0
for train, test in cv:    
	svc = linear_model.Ridge().fit(tr_x[train], tr_y[train,2])
	tr_score = tr_score + svc.score(tr_x[train], tr_y[train,2])
	te_score = te_score + svc.score(tr_x[test], tr_y[test,2])
print("train score: {0:.3f}, test score: {1:.3f}\n".format(tr_score/cv.n_iter, te_score/cv.n_iter))
endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' seconds used.\n'
    
print "linear model LinearRegression"    
starttime = datetime.datetime.now()    
tr_score,te_score=0.0,0.0
for train, test in cv:    
	svc = linear_model.LinearRegression().fit(tr_x[train], tr_y[train,2])
	tr_score = tr_score + svc.score(tr_x[train], tr_y[train,2])
	te_score = te_score + svc.score(tr_x[test], tr_y[test,2])
print("train score: {0:.3f}, test score: {1:.3f}\n".format(tr_score/cv.n_iter, te_score/cv.n_iter))
endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' seconds used.\n'
 
#print "SVR(kernel='linear',C=10,gamma=.01)"
#starttime = datetime.datetime.now()    
#tr_score,te_score=0.0,0.0
#for train, test in cv:
#	svc = svm.SVR(kernel ='linear', C = 10, gamma = .01).fit(tr_x[train], tr_y[train,2])
#	tr_score = tr_score + svc.score(tr_x[train], tr_y[train,2])
#	te_score = te_score + svc.score(tr_x[test], tr_y[test,2])
#print("train score: {0:.3f}, test score: {1:.3f}\n".format(tr_score/cv.n_iter, te_score/cv.n_iter))
#endtime = datetime.datetime.now()
#print str((endtime - starttime).seconds) + ' seconds used.\n'
 
print "Random Forest"    
starttime = datetime.datetime.now()    
tr_score,te_score=0.0,0.0
for train, test in cv:    
	svc = RandomForestRegressor(n_estimators = 3).fit(tr_x[train], tr_y[train,2])
	tr_score = tr_score + svc.score(tr_x[train], tr_y[train,2])
	te_score = te_score + svc.score(tr_x[test], tr_y[test,2])
print("train score: {0:.3f}, test score: {1:.3f}\n".format(tr_score/cv.n_iter, te_score/cv.n_iter))
endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' seconds used.\n'
 

print 'train model'
starttime = datetime.datetime.now()
regr = linear_model.LinearRegression()
regr.fit(tr_x,tr_y[:,2])
joblib.dump(regr, "model/model.m")
endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' seconds used.\n'


