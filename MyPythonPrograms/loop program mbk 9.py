# write a program to take any number from user and print addition of first and last digit


n = input("enter number")
n = int(n)
sum = 0
first = 0
last = n % 10
while n > 0:
    first = n % 10
    n = n // 10
print(last + first)
