class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_linkde_List:
    def __init__(self):
        self.head = None

    # Insert at head(beginnig)

    def insert_at_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert at end

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #  Insert at specific position

    def Insert_at_specific_position(self,pos,data):
        if pos == 0:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        current = self.head

        for i in range(pos-1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # Display the list

    def Display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")

sll = Singly_linkde_List()
sll.insert_at_head(10)
sll.Insert_at_specific_position(1,20)
sll.Insert_at_specific_position(2,30)
sll.append(30)
sll.Display()



            