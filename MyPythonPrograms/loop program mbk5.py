#write a program to take a no. from user and print its factorial value.

n= input("enter number", )
n=int(n)
i=1
sum=1
while i<=n:
    sum=sum*i
    i=i+1
print("fact value is",sum )

