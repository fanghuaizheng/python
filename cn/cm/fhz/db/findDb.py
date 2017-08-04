#coding=utf-8

import MySQLdb

url = '114.215.151.127'
username = 'root'
password='WANG199000zz'
database = 'test'

db = MySQLdb.connect(url,username,password,database,charset='utf8')

cursor = db.cursor()

sql = "select * from employee where income> '%d'" %(100)

try:
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        print row
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income)
except :
    print 'Error'


db.close()