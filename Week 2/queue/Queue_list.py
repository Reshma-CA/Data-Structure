def enqueue():
    num = int(input("enter a number:"))
    queue.append(num)
    print(num,"number added in the end")

def dequeue():
     if not queue:   # if len(queue) == 0: <=instead of this
        print("Queue is Empty")
     else:
        removed_element = queue.pop(0)
        print(removed_element,"Element removed front side")
        
def Display():
    if not queue:  # if len(queue) == 0:  <=instead of this
        print("Queue is Empty")
    else:
        print("Queue elements:")
        for item in queue:
            print(item)
        print("Front of the queue is:",queue[0])
        print("Rear of the queue is : ",queue[-1])
        
queue = []

while True:
    print("\nChoose an operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
        
    elif choice == '3':
        Display()
        
    elif choice == '4':
        print("wrong choice")
        break
    else:
        print("Exit loop")
       
# or

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
##################################################################

# using class
class Queue:
    def __init__(self):
        self.values = []
        
    def enqueue(self,x):
        self.values.append(x) # element add only End side
    def Dequeue(self):
        front = self.values[0] # element delete only front side
        self.values = self.values[1:]
        return front
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.values)
print(q.Dequeue())