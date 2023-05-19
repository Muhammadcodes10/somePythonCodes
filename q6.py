n = int(input("Enter a number between 0 and 100: "))

for i in range(2, n):
    if n/2 % i == 0:
        print(n, "is not a prime number")
        exit()
print(n, "is a prime number")