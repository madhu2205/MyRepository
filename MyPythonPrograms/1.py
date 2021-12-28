
class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def __add__(self, other):
        temp = point(0,0)
        temp.x=self.x+other.x
        temp.y=self.y+other.y
        return  temp

    def show(self):
        print(self.x,self.y)


p1=point(10,20)
p2=point(30,40)
p3=p1+p2
p3.show()