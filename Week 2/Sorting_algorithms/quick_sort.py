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

# 1. Pivot as First Element
def quick_sort_first(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # first element
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort_first(left) + [pivot] + quick_sort_first(right)

Arr = [10,2,5,9,1,7,4]
result = quick_sort_first(Arr)
print(result)  # Answer : [1, 2, 4, 5, 7, 9, 10]

# 2. Pivot as Last Element
def quick_sort_last(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[-1]
        
    left = [x for x in arr[:-1] if x < pivot ] # arr[:-1] --> Exclude pivot value
    right = [x for x in arr[:-1] if x >= pivot]
    
    return quick_sort_last(left)+[pivot]+quick_sort_last(right)
    
Arr = [10,2,5,9,1,7,4]
result = quick_sort_last(Arr)
print(result)  # Answer : [1, 2, 4, 5, 7, 9, 10]

# 3. Pivot as Middle Element
def quick_sort_middle(arr):
    if len(arr) <= 1:
        return arr
    mid_index = len(arr) // 2
    pivot = arr[mid_index]  # middle element
    left = [x for i, x in enumerate(arr) if x < pivot and i != mid_index]
    right = [x for i, x in enumerate(arr) if x >= pivot and i != mid_index]
    return quick_sort_middle(left) + [pivot] + quick_sort_middle(right)

Arr = [10,2,5,9,1,7,4]
result = quick_sort_middle(Arr)
print(result)  # Answer : [1, 2, 4, 5, 7, 9, 10]