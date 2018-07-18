import sys
sys.path.append('C:\\Users\\maxsagitov\\AppData\\Local\\Programs\\Python\\Python35-32\\preview')
from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='manager')
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=100000)
    print(tom.lastName())
    tom.giveRaise(.10)
    print(tom)
