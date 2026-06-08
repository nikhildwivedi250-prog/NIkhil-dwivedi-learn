arr = [11, 12, 33, 45, 67, 34, 899]
target = int(input("Enter your number: "))
found = False

for i in arr:
    if i == target:
        found = True
        break

if found:
    print("A khebadi mil gayo chho")
else:
    print("Dokara na mila chhe baba ")