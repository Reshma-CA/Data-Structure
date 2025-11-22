Array = [10,5,23,96,52,14,6,20] 

for i in range(1,len(Array)):
    key = Array[i]
    j = i-1
    
    while j>=0 and key<Array[j]:
        Array[j+1] = Array[j]
        j-=1
        
    Array[j+1] = key
    
print(Array)


##################################################################
# using function

def Insertion_sort(Array):
    for i in range(1,len(Array)):
        key = Array[i]
        j = i-1
        
        while j>=0 and key<Array[j]:
            Array[j+1] = Array[j]
            j-=1
            
        Array[j+1] = key
    return Array
    
Array = [10,5,23,96,52,14,6,20] 
result = Insertion_sort(Array)
print("Insertion sort result",result)