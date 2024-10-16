class single():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Hello my name is",self.name)
        print("My age is ",self.age)
x=single("Akshada",23)#creating object first
y=single("Vishwajeet",21)#creating object second
z=single("sangram",22)#creating object third
x.display()#calling function through fidrt object
y.display()#calling function through second object
z.display()#calling function through third object