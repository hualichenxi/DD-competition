#! /usr/bin/python

import MySQLdb
import numpy
import sys


try:    
	conn = MySQLdb.connect(host='localhost',port=3306, user='root', passwd='123456', db='ijcai')  
except Exception, e:  
    print e  
    sys.exit()

# s1='tr_d'
# s2='train'

# s1='va_d'
# s2='valid'


s1 = 'te_d'
s2 = 'test'

f0 = [s1+'_new','User_id','Location_id','Merchant_id']

if s1 != 'te_d':
	f0.append('Label')

#num=0
#tr_features = [f0, 
#	[s2+'_feature_buy_location','User_Location_count'],
#	[s2+'_feature_buy_merchant','User_Merchant_count'],
#	[s2+'_feature_buy_merchant_location','User_Merchant_Location_count'],
#	[s2+'_feature_location_buy_count','Location_buy_count'],
#	[s2+'_feature_location_merchant_count','Location_Merchant_count'],
#	[s2+'_feature_location_user_count','Location_User_count'],
#	[s2+'_feature_merchant_buy_count','Merchant_buy_count'],
#	[s2+'_feature_merchant_location_buy_count','Merchant_Location_count'],
#	[s2+'_feature_merchant_location_count','Merchant_Location_count'],
#	[s2+'_feature_merchant_location_user_count','Merchant_Location_User_count'],
#	[s2+'_feature_merchant_user_count','Merchant_User_count'],
#	[s2+'_feature_user_buy_count','User_buy_count'],
#	[s2+'_feature_user_location_count','User_Location_count'],
#	[s2+'_feature_user_merchant_count','User_Merchant_count'],
#	[s2+'_feature_taobao_user_click','Taobao_User_Click_count','Taobao_User_Buy_count'],
#]

num = 1
tr_features = [
	[s2+'_feature_buy_merchant_3days','User_Merchant_count'],
	[s2+'_feature_buy_merchant_7days','User_Merchant_count'],
	[s2+'_feature_buy_location_3days','User_Location_count'],
	[s2+'_feature_buy_location_7days','User_Location_count'],
	[s2+'_feature_buy_merchant_location_3days','User_Merchant_Location_count'],
	[s2+'_feature_buy_merchant_location_7days','User_Merchant_Location_count'],
]

print 'read data...'
arrs = []
for feature in tr_features:
	table = feature[0]
	atts = ','.join(feature[1:])
	sql = 'select ' + atts + ' from ' + table + ' order by User_id,Location_id,Merchant_id'
	print sql
	cur = conn.cursor()
	cur.execute(sql)
	res = cur.fetchall()
	arr = numpy.array(res)
	arrs.append(arr)
	cur.close()

print 'array merge...'
d = numpy.array(arrs[0])
for arr in arrs[1:]:
	d = numpy.concatenate((d,arr),axis=1)

print 'save to file...'
numpy.save('samples/'+s1+str(num),d)

conn.close()
