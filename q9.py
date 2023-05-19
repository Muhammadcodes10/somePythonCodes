import array as arr
num = int(input("Enter number please between 0 and 999: "))
strNum = len(str(num))
count = 0
sumIt = arr.array('i')
while strNum > 0:
    a = int((num % 10))
    sumIt.append(a)
    num /= 10
    strNum -= 1
    count += 1
print("The digits are:")
for i in range(len(sumIt), 0, -1):
    print(sumIt[i-1], end=' ')
print("\nThe number has", count, "digits")
