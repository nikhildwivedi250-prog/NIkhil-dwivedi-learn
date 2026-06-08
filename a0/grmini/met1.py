arr = [4, 8, 2, 11, 5, 23, 45, 6, 88, 33, 46]
x = 5
count = 0

for num in arr:
    if num > x:
        count += 1


print(count)