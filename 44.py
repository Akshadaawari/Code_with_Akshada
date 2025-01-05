#44.Write a Python class that implements a stack using OOP concepts.
class Stack:
    def __init__(self):
        self.items = [] 

   
    def is_empty(self):
        return len(self.items) == 0

    
    def push(self, item):
        self.items.append(item)

   
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

   
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

   
    def size(self):
        return len(self.items)

   
    def display(self):
        return self.items



stack = Stack()


stack.push(10)
stack.push(20)
stack.push(30)

print("Stack after pushes:", stack.display())  


print("Popped element:", stack.pop())  

print("Stack after pop:", stack.display()) 

print("Top element:", stack.peek())
  

print("Size of the stack:", stack.size()) 
