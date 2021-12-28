# write a program to take any number from user and print addition of its digit


n = input("enter number")
n = int(n)
sum = 0
while n > 0:
    b = n % 10
    sum = sum + b
    n = n // 10
print(sum)
