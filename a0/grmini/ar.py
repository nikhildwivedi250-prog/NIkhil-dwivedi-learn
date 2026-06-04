arr = [2, 3, 4, 5, 6, 7]
target = 3


for i in range(len(arr)):
    if arr[i] == target:
        ans = i
        break
print(ans)