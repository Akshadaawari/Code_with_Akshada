class comparision(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b 
    def show(self):
        if self.a> self.b:
            print("a is greater than b")
        elif self.a==self.b:
            print("both a and b have same value")
        else:
            print("b is greater than a")
        
object=comparision(4.0,4.0)
object.show()




