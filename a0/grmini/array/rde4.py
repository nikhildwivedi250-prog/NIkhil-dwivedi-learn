arr = [2, 4, 6, 8, 11]
is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break
print(is_sorted)