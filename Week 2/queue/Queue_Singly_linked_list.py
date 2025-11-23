class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to front of queue
        self.rear = None   # Points to rear of queue

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # If queue is empty, both front and rear are same
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} added to queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            # Queue becomes empty after removal
            self.rear = None
        print(f"{removed} removed from queue")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        current = self.front
        print("Queue elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


        
q = Queue()

q.enqueue(10)    # Output: 10 added to queue
q.enqueue(20)    # Output: 20 added to queue
q.enqueue(30)    # Output: 30 added to queue

q.display()      # Output: 10 -> 20 -> 30 -> None

q.dequeue()      # Output: 10 removed from queue
q.display()      # Output: 20 -> 30 -> None

#########################################################################
# more understandable

# queeue implimenting in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        
    def enqueue(self,data): # insert_at_End
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp =  self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        
    def dequeue(self): # delete at beginning
        self.head =  self.head.next
        
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
            
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.dequeue()
q.display()
