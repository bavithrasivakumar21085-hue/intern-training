# Creating class Student with 2 objects
class Student():
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def study(self):
        print(f"{self.name} is studing hard to get {self.grade} grade..!")
    

student1=Student("Bavithra", "A")
student2=Student("Kiruthiga", "A")

student1.study()
student2.study()