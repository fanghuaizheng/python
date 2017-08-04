#coding=utf-8
import MySQLdb

url = '114.215.151.127'
username = 'root'
password = 'WANG199000zz'
database = 'test'
db = MySQLdb.connect(url,username,password,database)

cursor = db.cursor();

# cursor.execute('select version()')

# data = cursor.fetchone()

# print 'Database version : %s' %data

#创建表
cursor.execute('drop table if EXISTS employee')

sql = """Create table employee (
         id INT (11) not NULL AUTO_INCREMENT,
         first_name VARCHAR (20) ,
         last_name VARCHAR(20),
         age int,
         sex VARCHAR(1),
         income FLOAT,
          PRIMARY KEY (id)
          )"""

cursor.execute(sql)

db.close()