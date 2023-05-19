import array as arr
num = int(input("Enter the size of student sample you need: "))
grades = arr.array('i')
for i in range(0, num):
    print("Enter student number", i+1, ":")
    val = int(input())
    grades.append(val)
Add = 0
for i in range(len(grades)):
    Add = Add + grades[i]
avg = Add/len(grades)

for i in range(len(grades)):
    if grades[i] > avg:
        print("Student Number", i, "Has Passed The Course")
    else:
        print("Student Number", i, "Has Failed The Course")
