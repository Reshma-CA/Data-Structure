Arr = [20,10,30,40,60,50]

target = 30

for i in range(len(Arr)):
    if target == Arr[i]:
        print(f"target found this position {i} and target value is {Arr[i]}")
        break

else:
    print("There is no target value")

#########################################################################

# using function
def Linear_search(arr,target):

    for i in range(len(arr)):
        if target == arr[i]:
            return f"target found this position {i} and target value is {arr[i]}"
          
    return -1
    
Arr = [20,10,30,40,60,50]
print(Linear_search(Arr,30))