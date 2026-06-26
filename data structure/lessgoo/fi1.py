num = [12, 45, 2, 89, 23]
target = num[0]

for ch in num:
    if ch > target:
        target = ch

print(target)