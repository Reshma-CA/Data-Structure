def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
        
    
    pivot = arr[-1]
    
    left = []
    right = []
    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
            
    return quick_sort(left)+[pivot]+quick_sort(right)
    
Arr = [10,2,5,9,1,7,4]
result = quick_sort(Arr)
print(result)  # Answer : [1, 2, 4, 5, 7, 9, 10]

# or
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[-1]
        
    left = [x for x in arr[:-1] if x < pivot ] # arr[:-1] --> Exclude pivot value
    right = [x for x in arr[:-1] if x >= pivot]
    
    return quick_sort(left)+[pivot]+quick_sort(right)
    
Arr = [10,2,5,9,1,7,4]
result = quick_sort(Arr)
print(result)  # Answer : [1, 2, 4, 5, 7, 9, 10]