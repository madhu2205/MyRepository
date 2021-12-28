
class A:
    def __init__(self):
        self.i=10
        print("In A")

class B(A):
    def __init__(self):
        super().__init__()
        self.j=20
        print("In B")
    def add(self):
        print(self.i+self.j)

ob=B()
ob.add()
