#coding=utf-8
from asyncore import dispatcher
from asynchat import async_chat
import asyncore,socket

PORT=5005
NAME="TestChart"

class ChatSession(async_chat):
    """
    处理单个用户与服务器之间联系
    """
    def __init__(self,sock):
        async_chat.__init__(self,sock)
        self.set_terminator('\r\n')
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        #处理获取的数据
        print line

class ChatServer(dispatcher):
    def __init__(self,port):
        #标准设置任务
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.session = []

    def handle_accept(self):
        conn,addr = self.accept()
        self.session.append(ChatSession(conn))

if __name__=='__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print "停止"


