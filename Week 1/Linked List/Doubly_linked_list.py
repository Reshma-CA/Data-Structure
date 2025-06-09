class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # points to previous node
        self.next = None  # points to next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty, set new_node as head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end and insert
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        print("Forward: ", end="")
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")
        
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.display_forward()
