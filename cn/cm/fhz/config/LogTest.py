import logging

logging.basicConfig(level=logging.INFO,filename=r'D:\logs\mylog.log')

logging.info('start program')

logging.info('Trying to devide 1 by 0')

print 1/0

logging.info('The division successded')

logging.info('Ending program')