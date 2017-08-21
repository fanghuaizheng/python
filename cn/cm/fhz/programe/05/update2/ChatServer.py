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
        meth = getattr(self,'do_'+cmd,None)
        try:
            meth(session,line)
        except TypeError:
            #如果不可以调用，此段代码相应位置命令
            self.unknown(session,cmd)


class Room(CommandHandler):
    """
    包括一个活着多个用户的范型环境，负责基本的命令处理与广播
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





