class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Singly_linked_List:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self,data):
        end_node = Node(data)
        if self.head is None:
            self.head = end_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = end_node
            
    def Display(self):
        current = self.head
        while current.next:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
            
Array = [10,20,30,40,50]
sll = Singly_linked_List()

for item in Array:
    sll.insert_at_end(item)
sll.Display()
        