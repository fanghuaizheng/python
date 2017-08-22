#coding=utf-8
from asyncore import dispatcher
from asynchat import async_chat
import  asyncore,socket

PORT=5005
NAME='TestRoom'
class EndSession(Exception):pass

class CommandHandler:
    """
    类似与标准库中的cmd.Cmd的简单命令处理
    """
    def unknown(self,session,cmd):
        session.push('unknown command: %s \r\n' %cmd)

    def handler(self,session,line):
        if not line.strip():return
        #分离命令
        parts = line.split(' ',1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        mname = 'do_'+cmd
        meth = getattr(self,mname,None)
        try:
            meth(session,line)
        except TypeError:
            #如果不可以调用，此段代码相应位置命令
            self.unknown(session,cmd)


class Room(CommandHandler):
    """
    包括一个或者多个用户的范型环境，负责基本的命令处理与广播
    """
    def __init__(self,server):
        self.server = server
        self.session = []

    def add(self,session):
        self.session.append(session)

    def remove(self,session):
        self.session.remove(session)
    def broadcast(self,line):
        for session in self.session:
            session.push(line)

    def do_logout(self,session,line):
        '响应登出'
        raise EndSession

class LoginRoom(Room):
    """
    为刚连接上的用户准备房间
    """
    def add(self,session):
        Room.add(self,session)
        self.broadcast('Welcome to %s \r\n'%self.server.name)
    def unknown(self,session,cmd):
        session.push('Please login \nUse<nick> \r\n')

    def do_login(self,session,line):
        name = line.strip
        if not name:
            session.push('please enter a name')
        elif name in self.server.users:
            session.push('this name is used')
            session.push('please try other name')
        else:
            session.name = name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    """
    为刚链接上的用户准备房间
    """
    def add(self,session):
        self.broadcast(session.name+'has entered the room \r\n')
        self.server.users[session.name] = session
        Room.add(self,session)
    def remove(self,session):
        Room.remove(self,session)
        self.broadcast(session.name+'has out this room \r\n')

    def do_say(self,session,line):
        self.broadcast(session.name+": "+line+"\r\n")
    def do_look(self,session,line):
        #处理look命令，这个命令是查看谁在房间
        session.push('the following are in this room \r\n')
        for other in self.session:
            session.push(other.name+'\r\n')
    def do_who(self,session,line):
        #处理who命令，该命令查看谁登陆l
        session.push('The following are login :\r\n')
        for name in self.server.users:
            session.push(name+"\r\n")
class LogoutRoom(Room):
    """
    单用户准备的简单房间，用于将用户从服务器出名
    """
    def add(self,session):
        try:
            del self.server.users[session.name]
        except KeyError:pass
class ChatSession(async_chat):
    """
    单会话，负责与用户的通信
    """
    def __init__(self,server,sock):
        async_chat.__init__(self,sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        self.name = None
        #所有的会话都开始于一个单独的房间
        self.enter(LoginRoom(server))

    def enter(self,room):
        #从当前房间移除自身，并且将自身加入到下一个房间
        try:
            cur = self.room
        except AttributeError:
            pass
        else:cur.remove(self)
        self.room = room
        room.add(self)
    def collect_incoming_data(self, data):
        self.data.append(data)
    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handler(self,line)
        except EndSession:
            self.handle_close()
    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LoginRoom(self.server))

class ChatServer(dispatcher):
    """
    只有一个房间的聊天器
    """
    def __init__(self,port,name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn,addr =self.accept()
        ChatSession(self,conn)

if __name__=='__main__':
    s = ChatServer(PORT,NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print '停止'




