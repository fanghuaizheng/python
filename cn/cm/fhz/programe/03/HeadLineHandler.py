from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadLineHandler(ContentHandler):
    in_headline = False
    def __init__(self,headline):
        ContentHandler.__init__(self)
        self.headline = headline
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name=='h1':
            text = ''.join(self.data)
            self.data = []
            self.headline.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


headlines = []

parse('website.xml',HeadLineHandler(headlines))

print 'The following <h1> elements were found:'

for h in headlines:
    print h
