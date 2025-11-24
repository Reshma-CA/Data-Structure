class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert at specific position (0-based index)
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List empty")
            return
        self.head = self.head.next

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("List empty")
            return
        if self.head.next is None:   # only 1 node
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None  # last node removed

    # Delete at position (0-based index)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List empty")
            return

        if pos == 0:
            self.delete_at_beginning()
            return

        temp = self.head
        for i in range(pos - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        delete_node = temp.next
        if delete_node is None:
            print("Position out of range")
            return

        temp.next = delete_node.next
        delete_node.next = None

    # Display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


# Example usage
sll = Singly()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_at_end(30)
sll.insert_at_position(1, 50)
sll.delete_at_beginning()
sll.delete_at_end()
sll.delete_at_position(1)
sll.display()
