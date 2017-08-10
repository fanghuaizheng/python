class NewsAgent:
    def __init__(self):
        self.sources = []
        self.destinations = []

    def addDestination(self,des):
        self.destinations.append(des)

    def addSource(self,source):
        self.sources.append(source)