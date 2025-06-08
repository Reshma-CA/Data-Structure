class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Singly_Linked_list:
    def __init__(self):
        self.head = None
        
    def insertion_fun(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        temp = self.head
        while temp :
            print(temp.data,end=" => ")
            temp = temp.next
                
sll = Singly_Linked_list()
sll.insertion_fun(30)
sll.insertion_fun(20)
sll.insertion_fun(10)
sll.display()