number = [1, 2, 5, 3, 4]
n = len(number)

for i in range(n):
    swapped = False

    for j in range(n-i-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1], number[j]
            swapped = True

    if swapped == False:
        print(f"list {i+1} par sorte ho gayi")
        break

print("sorted list :- ", number)