class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    #  Deletion at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is already empty")
        else:
            self.head = self.head.next
            
    # Deletion at specific position
    def delete_at_specific_position(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        
            
    #  Deletion at End
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
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)
sll.delete_at_beginning()
sll.delete_at_specific_position(3)
sll.display()         # Output: 20 -> 30 -> 50 -> None


sll.pop()
sll.display()         # Output: 20 -> 30 -> None
