#write a program to print fibonacci series for given number of terms

#program to show fibonacci series

n= input("enter how many terms fibonacci series u want to print..")
n= int(n)
prev=0
next=1
print (prev,next,end='')
i=1
while i<=n:
    r=prev+next
    print (r,end='')
    prev=next
    r=next
    print(r)
    i=i+1