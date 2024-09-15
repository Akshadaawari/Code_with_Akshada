class Parent(object):
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def display(self):
        print(self.name,self.surname)
class child(Parent):
    def __init__(self,c_name,c_dob,name,surname):
        self.c_name=c_name
        self.c_dob=c_dob

        Parent.__init__(self,name,surname)
    def show(self):
        print(self.c_name,self.c_dob)

obj=child('Akshada',26,"Rajaram","Awari")
obj1=Parent("Rajaram", "Awari")
obj.display()
obj.show()
obj1.display()