from xml.sax.handler import ContentHandler
from xml.sax import parse
import os
# import Dispatcher
class Dispatcher:
    def startElement(self,name,attrs):
        self.dispatch('start',name,attrs)
    def endElement(self,name):
        self.dispatch('end',name)

    def dispatch(self,prefix,name,attrs=None):
        mname = prefix+name.capitalize()
        dname = 'default'+name.capitalize()
        method = getattr(self,mname,None)
        if callable(method):args = ()
        else:
            method = getattr(self,dname,None)
            args = name
        if prefix=='start':
            args = ()
            if len(attrs.items())>0:
                args+=attrs,
        if callable(method):method(*args)

class WebsiteConstructor(Dispatcher,ContentHandler):
    passthrough = False

    def __init__(self,directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path):os.makedirs(path)

    def characters(self, content):
        if self.passthrough:
            self.out.write(content)

    def defaultStart(self,name,attrs):
        if self.passthrough:
            self.out.write('<'+name)
            for key,va in attrs.items():
                self.out.write(' %s="%s"' %(key,va))
            self.out.write('>')

    def defaultEnd(self,name):
        if self.passthrough:
            self.out.write('</%s>'%name)

    def startDirectory(self,attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectoty(self):
        self.directory.pop()

    def startPage(self,attrs):
        filename = os.path.join(*self.directory+[attrs['name']+'.html'])
        self.out = open(filename,'w')
        self.writerHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writerFooter()
        self.out.close()

    def writerHeader(self,title):
        self.out.write("<html>\n<head>\n<title>")
        self.out.write(title)
        self.out.write("</title>\n</head>\n<body>")

    def writerFooter(self):
        self.out.write("\n</body></html>\n")

parse('../website.xml',WebsiteConstructor('public_html'))