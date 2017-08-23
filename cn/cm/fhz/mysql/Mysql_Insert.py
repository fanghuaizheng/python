from __future__ import print_function
from datetime import date,datetime,timedelta
import mysql.connector

DB_NAME='employees'
username = 'root'
password='WANG199000zz'
host = '114.215.151.127'

cnx = mysql.connector.connect(user=username,password=password,host=host,database=DB_NAME)
cursor = cnx.cursor()

tomorrow = datetime.now().date()+timedelta(days=1)
#
# ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")

add_employee = (
    "insert into employees "
    "(first_name,last_name,hire_date,gender,birth_date) "
    "values (%s,%s,%s,%s,%s)"
)
data_employee = ('Geert12', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

cursor.execute(add_employee,data_employee)
emp_no = cursor.lastrowid

print(emp_no)

cnx.commit()
cursor.close()
cnx.close()