def fibanacci(n):
    if n<=1:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)

for item in range(10):
    print(fibanacci(item))




