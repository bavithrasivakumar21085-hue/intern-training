# Animal base classs and speak method, dag and cat base classes that overrides speak()
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Sound")
class Dog(Animal):
    def speak(self):
        print(self.name,"Bark")
class Cat(Animal):
    def speak(self):
        print(self.name,"Meow")
dog1=Dog("Dobby")
dog1.speak()

cat1=Cat("Cat")
cat1.speak()

animals=[dog1,cat1]
for x in animals:
    x.speak()

#Program 2 with bass class Shape with rectangle and circle child class using __str__ and super()
class Shape:
    def __init__(self,width,height):
        self.width= width
        self.height=height
    def area(self):
        print(self.width * self.height)
   

class Rectangle(Shape):
    def __init__(self,width,height):
      super().__init__(width,height)
    def __str__(self):
        return f"the width of the rectangle is {self.width},the height of the rectangle is {self.height}"
class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        print((22/7)* self.radius **2)
         
rec1= Rectangle(2,3)
rec1.area()
cir=Circle(6)
cir.area()

print(rec1)