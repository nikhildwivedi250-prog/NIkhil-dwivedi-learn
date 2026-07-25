def square(num):
    return num * num

num = int(input("Enter number for square :- "))

print("square :", square(num))

print("******* name reverse ********")
name = input("Enter your name :- ")

print(name[::-1])

print("======== sum number =========")

l = [10, 43, 44, 67, 45, 100]

print("Sum :", sum(l))

numb = [1, 3, 45, 67, 33]

print("max :", max(numb))


name = input("Enter yor name : ")

with open("kala.txt", "w") as file:
    file.write(name)

with open("kala.txt", "r") as file:
    print(file.read())