num = int(input("Enter a number between 0 and 1000: "))
count = 0
i = 0
while i < 3:
    if num < 0 or num > 1000:
        print("Error, Invalid input")
        exit()
    count = count + (num % 10)
    num = int(num / 10)
    i = i + 1

print("The sum is: ", count)
