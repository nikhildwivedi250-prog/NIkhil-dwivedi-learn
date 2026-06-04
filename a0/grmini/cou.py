arr = [3, 4, 5, 4, 6, 4, 7, 3, 5]
target = 4
count = 0

for i in arr:
    if i == target:
        count += 1
print(count)