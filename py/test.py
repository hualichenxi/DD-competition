#! /usr/bin/python
import numpy
import datetime
from sklearn.externals import joblib
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

def loadTestT(s):
	f = open(s)
	lines = f.readlines()
	f.close()
	a = [l.replace('\x01','').strip() for l in lines]
	return a


#fs = ['gap1','gap2','gap3','ifmpeak','ifepeak','iffestival','ifweekday','dayofweek','dayofweekday']
fs = ['gap1','gap2','gap3','gap_average','gap_latest']

print 'load data'
te_t = loadTestT('../data/test_t/000000_0')

te_x = numpy.empty([len(te_t),0])

for f in fs:
	te = loadColumns('../data/test_x_'+f+'/000000_0')
	te_x = numpy.concatenate((te_x,te),axis=1)
print "feature shape ", te_x.shape
print "target shape", len(te_t)
print 'testing ...\n'

starttime = datetime.datetime.now()
regr = joblib.load("model/model.m")
te_y = regr.predict(te_x)

endtime1 = datetime.datetime.now()
print str((endtime1 - starttime).seconds) + ' seconds used.\n'


f = open('results_5.csv','w')
for i,y in enumerate(te_y):
	o = te_t[i]+','+str(y) + '\n'
	f.write(o)
f.close()



