#write a program to take a progra from user and check that the no. is prime or not

n=input ("enter number:")
n= int(n)
i=2
while i<n:
    if n%i==0:
        print ("not prime number")
        break
    i=i+1
if i==n:
    print ("prime number")
