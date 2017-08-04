#coding=utf-8

import MySQLdb

url = '114.215.151.127'
username = 'root'
password='WANG199000zz'
database = 'test'

db = MySQLdb.connect(url,username,password,database,charset='utf8')

cursor = db.cursor()

#插入语句
sql = """insert into employee(first_name,last_name,age,sex,income) 
         values ('Mac','方怀正',28,'M',1800)"""

sql1 = "insert into employee (first_name,last_name,age,sex,income)  \
        values ('%s','%s','%d','%c','%d')" %('Mac','方怀正',
                                             27,'M',2900)

try:
    cursor.execute(sql1)
    db.commit()
except :
    print '错误了'
    db.rollback()

db.close()