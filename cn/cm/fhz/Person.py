_metaclass=type
class Person:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello world,I'm %s"%self.name\

foo = Person()
bee = Person()

foo.setName("foo")

bee.setName("bee")

foo.greet()

bee.greet()

print foo.name