from time import localtime,time,strftime
from nntplib import NNTP
import logging

logging.basicConfig(level=logging.INFO,filename=r'D:\logs\python\project3.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

day = 24*60*60

yesterday = localtime(time()-day)

date = strftime('%y%m%d',yesterday)

hour = strftime('%H%M%S',yesterday)

servername = 'news.aioe.org'
group ='comp.lang.python'

server = NNTP(servername)

ids = server.newnews(group,date,hour)[1]

logging.info('this is ids')
logging.info(ids)

for id in ids:
    print 'this is id',id
    head = server.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break

    body = server.body(id)[3]
    print subject
    print '-'*len(subject)
    print '\n'.join(body)

server.quit()
