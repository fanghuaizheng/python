#coding=utf-8
import platform
from ConfigParser import ConfigParser
import urllib


CONFIG_FILE_PATH='python.txt'

config = ConfigParser()

config.read(CONFIG_FILE_PATH)

osType = platform.system()

logpath = ''
if osType=='Windows':
    logpath = 'Windows'
elif osType=='Linux':
    logpath = 'others'
elif osType == 'Os':
    logpath = 'os'
else:logpath = 'others'

print 'os Type is :',config.get('logpath',logpath)

logfilepath = config.get('logpath',logpath)

log = open(logfilepath+'logfile.txt','w')

url = 'http://www.swig.org'

print >> log,('Downloading file from URL %s' % url)

text = urllib.urlopen(url).read()

print >> log,'File successfully downloaded'
