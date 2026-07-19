name = input("Please enter your name :- ")

print(name[::-1])
print(len(name))
print(name.upper())
print(name.lower())

password = input("Inter your password (password length is 6 digit) :-  ")

if len(password) >= 6 and len(password) < 7:
    print("Strong passwerd")
else:
    print("weak password")