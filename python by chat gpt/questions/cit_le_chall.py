name1 = input("Enter name 1 : ")
name2 = input("Enter name 2 : ")
name3 = input("Enter name 3 : ")
name4 = input("Enter name 4 : ")
name5 = input("Enter name 5 : ")

with open("student.txt", "w") as file:
    file.write("name1 :" + name1 +"\n")
    file.write("name2 :" + name2 +"\n")
    file.write("name3 :" + name3 +"\n")
    file.write("name4 :" + name4 +"\n")
    file.write("name5 :" + name5 +"\n")
with open("student.txt", "r") as file:
    print(file.read())