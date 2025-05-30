Arr = [10,20,30,40,50,60]

def binary_search(arr):
    target = 30
    left = 0
    right = len(arr)-1
    

    while(left<=right):
        mid = left+right//2
        if Arr[mid] == target:
            print(f"Found target at this index position {mid} and value {Arr[mid]}")
            break

        elif arr[mid]>target:
            right = mid-1

        else:
            left = mid+1

    if(left>right):
        print("Target element not found in this array")

#############################################################################
# using function

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    

    while(left<=right):
        mid = left+right//2
        if arr[mid] == target:
            return f"Found target at this index position {mid} and value {arr[mid]}"
            # break

        elif arr[mid]>target:
            right = mid-1

        else:
            left = mid+1
            
    return -1
    
Arr = [10,20,30,40,50,60]
print(binary_search(Arr,30))
    
#######################################################################
            

"""

Binary search is a divide-and-conquer algorithm that is highly efficient for large datasets because 
it reduces the search space by half in each step. This makes it significantly faster than linear search
for sorted data.

The time complexity : O(log n)

"""