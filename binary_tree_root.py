class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def Print_Tree(self):
        print(self.data)
root=Node(10)
root.Print_Tree()