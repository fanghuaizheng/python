from nntplib import NNTP
from time import strftime,time,localtime
from email import message_from_string
from urllib import urlopen
import re
import textwrap

day = 24*60*60

def wrap(string,max=70):
    """
    将字符串调整为最大行宽
    :param string:
    :param max:
    :return:
    """
    return '\n'.join(textwrap.wrap(string))+'\n'

class NewsAgent:
    """
    可以从新闻来源获取新闻项目并且发布到新闻目标的对象。
    """
    def __init__(self):
        self.sources=[]
        self.destinations=[]
    def addSource(self,source):
        self.sources.append(source)
    def addDestination(self,dest):
        self.destinations.append(dest)
    def distribute(self):
        """
        从所有来源获取所有新闻并且发布到所有目标
        :return:
        """
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)

class NewsItem:
    """
    包括标题和主体文本的简单新闻项目
    """





