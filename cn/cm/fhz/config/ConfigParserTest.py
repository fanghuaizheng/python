#coding=utf-8
from ConfigParser import ConfigParser
CONFIGFILE='python.txt'

config = ConfigParser()
#读取配置文件
config.read(CONFIGFILE)
# 要查看的区域段是message
# 打印初始化的问候语
print config.get('message','greeting')

radius = input(config.get('message','question')+'')

print config.get('message','result_message')

print config.getfloat('numbers','pi')*radius*2
