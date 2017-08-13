from asyncore import dispatcher
import socket,asyncore

PORT = 5005


class ChartServer(dispatcher):

    def __init__(self,port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', 5005))
        self.listen(5)


    def handle_accept(self):
        conn,addr = self.accept();
        print 'Connecting from address',addr[0]



if __name__=='__main__':
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print '键盘停止'
