class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Link to the previous node
        self.next = None  # Link to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

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

    # 3. Insert at specific position (0-based index)
    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
       
        for i in range(1,pos-1):
             temp = temp.next
             if temp is None:
                print("Index out of range")
                return
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

       

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")


# Example Usage
dll = DoublyLinkedList()

dll.insert_at_beginning(30)      # List: 30
dll.insert_at_beginning(20)      # List: 20 <=> 30
dll.insert_at_end(40)            # List: 20 <=> 30 <=> 40
dll.insert_at_position(2, 25)    # List: 20 <=> 30 <=> 25 <=> 40
dll.insert_at_position(0, 10)    # List: 10 <=> 20 <=> 30 <=> 25 <=> 40

dll.display()
