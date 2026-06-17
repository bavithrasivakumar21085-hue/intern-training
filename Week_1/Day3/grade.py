#check what grade the mark gets
mark = int(input("Enter your mark:"))
if mark >= 90:
    print("A Grade")
elif mark >= 75:
    print("B Grade")
elif mark >= 60:
    print("C Grade")
elif mark >= 40:
    print("D Grade")
else:
    print("Fail")