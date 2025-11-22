Array = [10,5,23,96,52,14,6,10]

n = len(Array)

for i in range(n):
    for j in range(n-i-1):
        if Array[j]>Array[j+1]:
            temp = Array[j]
            Array[j]= Array[j+1]
            Array[j+1] = temp

print("Bubble sorted result:",Array)

######################################################

# using function

def Bubble_sorted_array(Array):

    n= len(Array)
    for i in range(n):
        for j in range(n-i-1):
            if Array[j]>Array[j+1]:
                Array[j],Array[j+1] = Array[j+1],Array[j]
    return Array
    
Array = [10,5,23,96,52,14,6,10]
result = Bubble_sorted_array(Array)
print("Bubble sorted result:",result)