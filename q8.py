num = int(input("Enter a number: "))
if num % 5 == 0 or num % 6 == 0:
    if num % 5 == 0 and num % 6 != 0:
        print("The number is only divisible by 5")
    elif num % 6 == 0 and num % 5 != 0:
        print("The number is only divisible by 6")
    else:
        print("The number is divisible by both")
else:
    print("The number is divisible by neither")

