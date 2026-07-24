print("----largest number----")

a = int(input("Enter your First number :- "))
b = int(input("Enter your Second number :- "))
c = int(input("Enter your Third number :- "))

if a >= b and a >= c:
    print("largest : ", a)
elif b >= a and b >= c:
    print("largest : ", b)
else:
    print("largest : ", c)


print("=====positive_negative_zero=====")

n = int(input("Enter number : "))

if n < 0:
    print("Negative")
elif n > 0:
    print("Positive")
else:
    print("Zero")


print("//////////area of Rectangle/////////")

length = float(input("Enter length : "))
width = float(input("Enter width : "))

area = length * width

print("Area : ", area)


print("####### Simple calculator #######")

x = float(input("FIrst number : "))
y = float(input("Second number : "))

print("Add = ", x+y)
print("Sub = ", x-y)
print("mul. = ", x*y)

if y != 0:
    print("divi. = ", x/y)
else:
    print("0 se divide nhi kar sakate")


print("THANK YOU")