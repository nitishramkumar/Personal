class Parent(object):
    def altered(self):
        print("Parent Altered")

class Child(Parent):
    def altered(self):
        print("Child Altered")
        super(Child,self).altered();
        print("Child Altered again")

par = Parent()
son = Child()
par.altered()
son.altered()
