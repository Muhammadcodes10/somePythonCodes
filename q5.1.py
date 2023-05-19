
size = int(input("Enter the sample size: "))
num = int(input("Enter the number, please: "))
myMin = myMax = num
myMinText = "Input number 1 is the Min"
myMaxText = "Input number 1 is the Max"
count = size + 1
while size > 1:
    num = int(input("Enter another number, please: "))
    if num < myMin:
        myMin = num
        myMinText = "Input number", (count - size), "is the Min"
    if num > myMax:
        myMax = num
        myMaxText = "Input number", (count - size), "is the Max"
    size = size - 1

print("The Min number is:", myMin)
print(myMinText)
print("The Max number is:", myMax)
print(myMaxText)
