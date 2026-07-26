s = input("Enter character name : ")
print(len(s))

name = input("Enter your name : ")
count = 0

for ch in name:
    if ch.lower() in "aeiou":
        count += 1

print(count)

print("^^^^largest number^^^^")

num = [10, 34, 53, 33, 55, 5]
target = num[0]

for i in range(6):
    numb = int(input("Enter your number: "))
    num.append(numb)

print("largest: ", max(num))