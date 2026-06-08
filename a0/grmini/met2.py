arr = [2, -3, 4, -5, -4, 3, -8, -1]

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print(arr)