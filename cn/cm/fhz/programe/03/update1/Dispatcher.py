import os
class Dispatcher:
    def startElement(self,name,attrs):
        self.dispatch('start',name,attrs)
    def endElements(self,name):
        self.dispatch('end',name)

    def dispatch(self,prefix,name,attrs=None):
        mname = prefix+name.capitalize()
        dname = 'default'+name.capitalize()
        method = getattr(self,mname,None)
        if callable(method):args = ()
        else:
            method = getattr(self,dname,None)
            args = name
        if prefix=='start':args+=attrs
        if callable(method):method(*args)

    def writerHeader(self,title):
        self.out.writer("<html>\n<head>\n<title>")
        self.out.writer(title)
        self.out.writer("</title>\n</head>\n<body>")

    def writerFooter(self):
        self.out.writer("\n</body></html>\n")

    def defaultStart(self,name,attrs):
        if self.passthrough:
            self.out.writer('<'+name)
            for key,va in attrs.items():
                self.out.writer(' %s="%s"' %(key,va))
            self.out.writer('>')

    def defaultEnd(self,name):
        if self.passthrough:
            self.out.writer('</%s>'%name)

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path):os.makedirs(path)
