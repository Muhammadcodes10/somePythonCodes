print("OPTION 1: BINARY TO BASE 10 \n"
      "OPTION 2: BASE 10 TO BINARY \n"
      "\nSELECT AN OPTION: ", end="")
select = int(input())
if select == 1:
    number = int(input("Enter a binary number: "))
    n = 0
    count = 0
    while number > 0:
        count = count + ((number % 2) * 2 ** n)
        number = int(number / 10)
        n = n + 1
    print("The corresponding value in base 10 is: ", count)
elif select == 2:
    number = int(input("Enter a base 10 number: "))
    count = ''
    while number > 0:
        temp = str((number % 2))
        count = count + temp
        number = int(number / 2)
    i = len(count) - 1
    print("The corresponding value in binary is: ", end='')
    while i >= 0:
        print(count[i], end='')
        i = i - 1
    print("\n")
else:
    print("Select a valid option!")