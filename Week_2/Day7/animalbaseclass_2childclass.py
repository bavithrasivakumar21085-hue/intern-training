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