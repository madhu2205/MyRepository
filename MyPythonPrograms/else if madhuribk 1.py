#print max number out of 3 number
a= input("enter number 1:")
b=input("enter number 2:")
c= input("enter number 3:")
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print(a,"is max")
elif b>a and b>c:
    print(b,"is max")
else:
    print(c,"is max")