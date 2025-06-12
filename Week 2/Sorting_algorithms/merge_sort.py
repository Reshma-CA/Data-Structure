def merge(li1, li2):   # the main merge funtion that is used to merge two sorted array
    result = []
    i = j = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            result.append(li1[i])
            i += 1
        else:
            result.append(li2[j])
            j += 1
    result.extend(li1[i:])
    result.extend(li2[j:])
    return result    # returns the sorted array as a new array named "result"


def merge_sort(arr):
    if len(arr) == 1:  # recursion base case thats the length of the array became 1
        return arr      # returns the array with array size 1
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left = merge_sort(left_half )
    right = merge_sort(right_half)
    return merge(left, right)
    
Array = [78,2,45,4,95,11,53,6,77,100]
result_array = merge_sort(Array)
print(result_array) # explain code line by line