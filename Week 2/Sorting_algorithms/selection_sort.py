Arr = [10,20,30,40,50,60]

target = 30
left = 0
right = len(Arr)-1
   

while(left<=right):
    mid = left+right//2
    if Arr[mid] == target:
        print(f"Found target at this index position {mid} and value {Arr[mid]}")
        break

    elif Arr[mid]>target:
        right = mid-1

    else:
        left = mid+1

if(left>right):
    print("Target element not found in this array")
        

