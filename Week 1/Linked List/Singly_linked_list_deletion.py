class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is already empty")
        else:
            self.head = self.head.next
            
    def delete_at_specific_position(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        
            
    def pop(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
       
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
sll = SinglyLinkedList()
sll.insert_at_head(40)
sll.insert_at_head(30)
sll.insert_at_head(20)
sll.insert_at_head(10)
sll.insert_at_head(5)
sll.delete_at_beginning()
sll.delete_at_specific_position(3)
sll.display()         # Output: 10 -> 20 -> 40 -> None


sll.pop()
sll.display()         # Output: 10 -> 20 -> None
