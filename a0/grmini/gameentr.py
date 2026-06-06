age = int(input("What is your age: "))

condition = input("kya aapke pass parental permission hai? (yes/no): ")


if age >= 18 or ( age > 13 and condition == "yes"):
    print("Welcome yor are play this GAME10")
else:
    print("Sorry you don't play this GAME")