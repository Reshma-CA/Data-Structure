Arr = [20,10,30,40,60,50]

target = 30

for i in range(len(Arr)):
    if target == Arr[i]:
        print(f"target found this position {i} and target value is {Arr[i]}")
        break

else:
    print("There is no target value")