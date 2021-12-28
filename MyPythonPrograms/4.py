class Human:
    def talk(self):
        print("Hello")

class Duck:
    def bark(self):
        print("Quack Quack")

class Dog:
    def bark(self):
        print("Bow Bow")

def show(ob):
    if hasattr(ob,'talk'):
        ob.talk()
    else:
        ob.bark()

t1=Human()
t2=Duck()
t3=Dog()
show(t1)
show(t2)
show(t3)