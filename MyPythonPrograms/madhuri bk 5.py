#write a program to take 3 digit from user & print addition of its digit


a=input("enter 3 digit number")
a= int(a)
b=a//100
c=a%100
d=c//10
e=c%10
f=b+d+e
print (f)