class A(object):
    def __str__(self):
        return  "This is object of A class"

class B(A):
    def __str__(self):
        return "This is object of B class"

ob1=A()
ob2=B()
print(ob1.__str__())
print(ob2)