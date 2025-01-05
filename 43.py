#43.Write a Python program to implement inheritance and method overriding
class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
       
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed  

   
    def speak(self):
        return f"{self.name} barks"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) 
        self.color = color  
   
    def speak(self):
        return f"{self.name} meows"


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")


print(dog.speak())  
print(cat.speak())  