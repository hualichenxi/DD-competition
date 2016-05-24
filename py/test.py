#! /usr/bin/python
import numpy
import datetime
from sklearn.externals import joblib

starttime = datetime.datetime.now()

print 'testing ...\n'
te_f0 = numpy.load('samples/te_d0.npy')
te_f1 = numpy.load('samples/te_d1.npy')
te_d = numpy.concatenate((te_f0,te_f1),axis=1)

clf = joblib.load("model/model.m")
p = clf.predict(te_d[:,3:])
te_r = numpy.concatenate((te_d[:,0:3],p.reshape(p.shape[0],1)),axis=1)

endtime1 = datetime.datetime.now()
print str((endtime1 - starttime).seconds) + ' seconds used.\n'

print 'write results...'

m_r = {}
for item in te_r:
	key = str(item[0])+','+str(item[1])
	if m_r.has_key(key):
		arr = m_r[key]
		if item[3] == 1 and item[2] not in arr:
			arr.append(item[2])
			m_r[key] = arr
	else:
		if item[3] == 1:
			m_r[key] = [item[2]]
		else:
			m_r[key] = []

f = open('results.csv','w')

keys = m_r.keys()
for key in keys:
	line = key + ',' + ':'.join(str(i) for i in m_r[key])	
	f.write(line + '\n')
f.close()

endtime2 = datetime.datetime.now()
print str((endtime2 - endtime1).seconds) + ' seconds used.\n'
