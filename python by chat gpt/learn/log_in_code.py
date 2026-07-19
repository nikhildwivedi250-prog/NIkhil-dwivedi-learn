name = input("Inter your First name :- ")
middle = input("Inter your Middle name :- ")
last_name = input("Inter your Last name :- ")

password = input("inter your password (password duration 6 digit :- )")

if len(password) >= 6 and len(password) < 7:
    print("Strong password")
else:
    print("week password")

age = int(input("Inter your age :- "))

if age >= 18 and age < 100:
    print("Adult")
else:
    print("Minor")

mob_number = input("Inter your mobile number :- ")

if len(mob_number) <= 10 and len(mob_number) >= 10:
    print("connected")
else:
    print("Please inter a correct number ")
    input("Inter a correct number :- ")