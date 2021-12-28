class A:
    def __init__(self,x):
        self.i=x
        print("In A")


class B(A):
    def __init__(self,p,q):
        super().__init__(q)
        self.j=p
        print("In B")

    def add(self):
        print(self.i+self.j)


ob=B(100,200)
ob.add()

