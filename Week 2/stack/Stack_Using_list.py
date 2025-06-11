def push():
    num = int(input("Enter a number: "))
    stack.append(num)
    print(num,"is inserted in to stack")
    
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        removed_element = stack.pop()
        print(removed_element,"is deleted in the stack")
    
    
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        for item in reversed(stack):
            print(item)
    
stack = []
while True:
    print("\nChoose operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# or
stack = []
stack.append("Welcome")
stack.append("to")
stack.append("my")
stack.append("World")
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)