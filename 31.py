#31.Write a Python function to implement a stack with basic operations (push, pop, peek).
class Stack:
    def __init__(self):
      self.stack = []
    def push(self, item):
       self.stack.append(item)
    def pop(self):
       if not self.is_empty():
            return self.stack.pop()
       else:
            print("Stack is empty!")
            return None
    def peek(self):
       
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

# Test the Stack class
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.stack)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Stack after pop:", stack.stack)
    print("Is stack empty?", stack.is_empty())
    print("Stack size:", stack.size())
