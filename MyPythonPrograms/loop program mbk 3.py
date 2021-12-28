# write a program to print addition of all even  no. between 1 to 10


i = 1
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print("addition is", sum)
