import formats
from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
class Manager(Person):
    def __init__(self, name,pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    pet = Manager('Pet Fall', pay=100)
    tom = Manager('Tom Jones', 50000)

    print('--All there--')
    for object in (bob,sue, pet, tom):
        object.giveRaise(.10)
        print(object)

class Dep:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

#devel = Dep(bob, sue)
#devel.addMember(tom)
#devel.giveRaises(.10)
#devel.showAll()
