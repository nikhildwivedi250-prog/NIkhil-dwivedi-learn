# Discount calculator


name = input("Enter your coustmer name :-  ")
age = int(input("Enter your coustmer age :- "))
day = input("Inter the nsme of Day :- ")

if age <= 12 and day == "Friday":
    print("Congras aapko 35 taka discopunt milata hai")

elif age <= 18 and day == "Friday":
    print("congras aapko 33 taka discount milata hai")

elif age <= 40 and day == "Friday":
    print("congras aaapko 32 taka discount m,ilata hai")

elif age <= 100 and day == "Friday":
    print("congras aapko 38 taka discount milkata hai")

else:
    print("congras aapko 10 taka discount milata hai")