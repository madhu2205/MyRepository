#write a program to take 2 digit no. from user and print its reverse number

a= input("enter 2 digit number:")
a=int(a)
b=a//10
c=a%10
a=b+c*10
print(a)