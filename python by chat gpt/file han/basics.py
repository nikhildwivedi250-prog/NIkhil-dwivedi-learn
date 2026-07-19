file = open("notes.txt", "W")

file.write("hello, python I am nikhil dwivedi")

file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()