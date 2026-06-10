# check the given number is positive/negative/zero
number = int(input("Enter the number:"))
if number > 0:
    print("positive")
elif number == 0:
    print("Zero")
else:
    print("Negative Number")

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
#check whether the password is correct or not
password="python123"
entered=input("Enter the password")
if entered==password:
    print("Correct Password")
else:
    print("Invalid password")
    
#find the greatest of all three numbers
a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))
c= int(input("Enter 3rd number:"))
if a>b and a>c:
    print("Largest number is", a)
elif b>a and b>c:
    print("Largest number is", b)
else:
    print("Largest number is:", c)

