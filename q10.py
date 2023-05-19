def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


def raisePower(x, y):
    return x ** y


def largestPower():
    n = int(input("Enter the value of the number: "))
    x = int(input("Enter the value of x: "))
    if not isPrime(n):
        ans = 0
        for i in range(1, n + 1, 1):
            sol = raisePower(x, i)
            if n % sol == 0:
                ans = i
        print(ans, "is the largest divisor")
    else:
        print("The number is prime and we can't work with it!")


def primeDivisors():
    n = int(input("Enter the number, so we can find the primeDivisors: "))
    flag = True
    for i in range(2, n + 1):
        if isPrime(i):
            if n % i == 0:
                print(i, "is a prime divisor")
                flag = False
    if flag:
        print("The number has no prime divisor")


largestPower()
primeDivisors()
