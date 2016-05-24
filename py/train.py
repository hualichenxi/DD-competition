#! /usr/bin/python
import numpy
import datetime
from sklearn.externals import joblib
from sklearn import linear_model

fs = ['gap1','gap2','gap3','ifmpeak','ifepeak','iffestival','ifweekday']

print 'load data...\n'
tr_y = loadColumns('../data/train_y/000000_0')
tr_x = numpy.array([[]])
for f in fs:
	tr = loadColumns('../data/train_x_'+f+'/000000_0')
	tr_x = numpy.concatenate((tr_x,tr),axis=1)

starttime = datetime.datetime.now()
regr = linear_model.LinearRegression()
regr.fit(tr_x,tr_y[:,2])
joblib.dump(regr, "model/model.m")

endtime1 = datetime.datetime.now()
print str((endtime1 - starttime).seconds) + ' seconds used.\n'

def loadColumns(s):
	f = open(s)
	lines = f.readlines()
	f.close()
	a = []
	for line in lines:
		line = line.replace('\\N','0')
		a.append([float(i) for i in line.strip().split(' \x01')])
	return numpy.array(a)
