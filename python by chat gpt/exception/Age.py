try:
    age = int(input("Enter your age : "))
   # print("your age is :", age)
    
    if age >= 18:
        print(f"your age is {age} you are adult")

    else:
        print(f"your age is {age} you are minor")


except ValueError:
    print("Age must be a number")