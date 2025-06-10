class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            temp = self.head
            while temp.next != self.head:  # Traverse until the last node
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Make it circular

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

        
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.display()
