class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
         # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None
        
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
            
        before.next = temp.next
        temp.next.prev = before 
        temp.prev = None
        temp.next = None
        
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")
        
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.insert_at_end(60)

dll.delete_at_beginning()
dll.delete_at_end()

dll.delete_at_position(3)
dll.display()  # Answer :  20 <=> 30 <=> 50 <=> None

