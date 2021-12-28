#write a program to take 3 digit no. from user and print its reverse no.


a=input("enter 3 digit number:")
a=int(a)
b=a//100
c=a%100
d=c//10
e=c%10
f=b+d*10+e*100
print(f)