class animal(object):
    def __init__(self,animal_name,animal_type):
        self.animal_name=animal_name
        self.animal_type=animal_type
    def display(self):
        print(self.animal_name,self.animal_type)
class pet(animal):
    def __init__(self,cost,life_span,animal_name,animal_type):
        self.cost=cost
        self.life_span=life_span

        animal.__init__(self,animal_name,animal_type)
    def show(self):
        print(self.cost,self.life_span)

obj=animal("lion","carnivourus")  
obj.display()
obj2=pet("300000",5,"cat","carnivourus")
        