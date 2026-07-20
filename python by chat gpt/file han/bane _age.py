name = input("Enter your name : ")
age = input("Enter your age : ")

with open("student.txt", "w") as file:
    file.write("name: " + name +"\n")
    file.write("age: " + age)

print("Name and age save successfully")

with open("student.txt", "r") as file:
    data = file.read()

print("\nfile data")
print(data)