number = [12, 3, 45, 34, 11]

smallest = number[0]
largest = number[0]

for num in number:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("largest: ", largest)
print("smallest: ", smallest)