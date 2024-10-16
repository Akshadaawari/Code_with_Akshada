class Mobile():
    def __init__(self,Brand,price):
        self.Brand=Brand
        self.price=price
    def show(self):
        print("My mobiles brand name is",self.Brand)
        print("Price of this mobile",self.price)
for i in range(2):#for loop work same in function 
    obj=Mobile("Apple","50k")
    obj.show()

