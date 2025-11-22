Array = [10,5,23,96,52,14,6,20]

for i in range(len(Array)):
    min_pos = i
    for j in range(i+1,len(Array)):
        if Array[j]<Array[min_pos]:
            min_pos =j
            
    Array[i],Array[min_pos] = Array[min_pos],Array[i]
    
print("Selection Sort result: ",Array)

############################################################################
# using function

def selection_sort(Array):
    for i in range(len(Array)):
        min_pos = i
        for j in range(i+1,len(Array)):
            if Array[j]<Array[min_pos]:
                min_pos =j
                
        Array[i],Array[min_pos] = Array[min_pos],Array[i]
    return Array

Array = [10,5,23,96,52,14,6,20] 
result = selection_sort(Array)
print("Selection Sort result: ",result)