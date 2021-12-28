#write a program to print all the prime number between 1 to 100




n = 1
while n <= 100:
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print(n)
    n = n + 1
