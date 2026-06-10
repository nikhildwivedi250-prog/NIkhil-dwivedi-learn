arr = [10, 20, 30, 40, 50, 60]
target = 10
ans = -1

for i in range(len(arr)):
    if arr[i] == target:
        ans = i
        break

print(ans)