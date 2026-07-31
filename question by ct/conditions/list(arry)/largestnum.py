arr = [12, 44, 5, 66, 45, 4, 77]
target = arr[0]

for num in arr:
    if target < num:
        target = num

print("Target : ", target)