import Dispatcher
from xml.sax.handler import ContentHandler
from xml.sax import parse
class TestHandler(Dispatcher,ContentHandler):
    def startPage(self,attrs):
        print 'Beginning page',attrs['name']

    def endPage(self):
        print 'Ending page'

