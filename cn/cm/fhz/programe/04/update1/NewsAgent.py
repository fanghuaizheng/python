class NewsAgent:
    def __init__(self):
        self.sources = []
        self.destinations = []

    def addDestination(self,des):
        self.destinations.append(des)

    def addSource(self,source):
        self.sources.append(source)

    def distribute(self):
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)

class PlainDestination:
    def receiveItems(self,items):
        for item in items:
            print item.title
            print '-'.len(item.title)
            print item.body
