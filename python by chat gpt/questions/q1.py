print("Hello python")
print("Welcome to programming")

name = input("Enter your name : ")
age = input("Enter your age : ")
city = input("Enter your city name : ")

print("---Add number---")
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Sum :-", a+b)

print("----Even and Odd----")

num = int(input("Enter your number :- "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


print("-----Table-----")

nums = int(input("Enter your number for table :- "))

for i in range(1, 11):
    print(nums, "*", i, "=", nums*i)