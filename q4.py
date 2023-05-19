firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
thirdNumber = int(input("Enter the third number: "))

if firstNumber < secondNumber < thirdNumber:
    print(firstNumber, secondNumber, thirdNumber)
elif firstNumber < thirdNumber < secondNumber:
    print(firstNumber, thirdNumber, secondNumber)
elif secondNumber < firstNumber < thirdNumber:
    print(secondNumber, firstNumber, thirdNumber)
elif secondNumber < thirdNumber < firstNumber:
    print(secondNumber, thirdNumber, firstNumber)
elif thirdNumber < firstNumber < secondNumber:
    print(thirdNumber, firstNumber, secondNumber)
else:
    print(thirdNumber, secondNumber, firstNumber)