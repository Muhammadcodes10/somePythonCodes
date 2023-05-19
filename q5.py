def findMin():
    if f < s and f < t and f < fo:
        print("1st number is the Min")
    elif s < f and s < t and s < fo:
        print("2nd number is the Min")
    elif t < f and t < s and t < fo:
        print("3rd number is the Min")
    elif fo < f and fo < s and fo < t:
        print("4th number is the Min")


def findMax():
    if f > s and f > t and f > fo:
        print("1st number is the Max")
    elif s > f and s > t and s > fo:
        print("2nd number is the Max")
    elif t > f and t > s and t > fo:
        print("3rd number is the Min")
    elif fo > f and fo > s and fo > t:
        print("4th number is the Min")


f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
t = int(input("Enter the third number: "))
fo = int(input("Enter the fourth number: "))

findMin()
findMax()
