class Bt:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,data):
        if self.data:
            if self.data<self.data:
                if self.data is None:
                    self.left=data
                else:
                    self.left.insert(data)
            elif data> self.data:
                if self.right is None:
                    self.right=data
                else:
                    self.right.insert(data)
            else:
                self.data=data 
    def show(self):
        if self.left:
            self.left.show()
            print(self.data)
        if self.right:
            self.right.show()
            print(self.data)

root=Bt(12)
root.insert(10)
root.insert(4)
root.insert(6)
root.show()