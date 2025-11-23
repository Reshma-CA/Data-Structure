class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        
        
    def push(self,data):  # Insert at beginning
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
    def pop(self):  # Deletion at beginning
        if self.top is None:
            print("Empty stack")
            return None
        
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Poped Data is: {popped_data}")
        
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        print(f"Peek element is: {self.top.data}")
    
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()  # Answer: 50 -> 40 -> 30 -> 20 -> 10 -> None
s.pop()      # Answer: Poped Data is: 50
s.display()  # Answer: 40 -> 30 -> 20 -> 10 -> None
s.peek()     # Answer: Peek element is: 40

####################################################

# more understandable

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self,data): # insert_at_beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self): # delete_at_beginning
        self.head = self.head.next
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
            
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.display()

            
        
            
        