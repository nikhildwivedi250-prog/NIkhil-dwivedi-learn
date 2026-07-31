arr = [100, 32, 33, 55, 43]
small = arr[0]

for num in arr:
    if small > num:
        small = num 

print("Smallest : ", small)
