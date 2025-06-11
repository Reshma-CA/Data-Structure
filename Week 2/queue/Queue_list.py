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