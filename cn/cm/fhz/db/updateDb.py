#coding=utf-8

import MySQLdb

url = '114.215.151.127'
username = 'root'
password='WANG199000zz'
database = 'test'

db = MySQLdb.connect(url,username,password,database,charset='utf8')

cursor = db.cursor()

sql = "update employee set age=age+1 where sex='%c'" %('M')

try:
    cursor.execute(sql)

    db.commit()
except:
    db.rollback()
db.close()