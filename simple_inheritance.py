class parents():
    def __init__(self,surname):
        self.surname=surname
    def show(self):
        print("Your surname is",self.surname)
class child(parents):
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Your good name is",self.name)
obj=child("Akshada")
obj1=parents("Awari")
obj.display()
obj1.show()