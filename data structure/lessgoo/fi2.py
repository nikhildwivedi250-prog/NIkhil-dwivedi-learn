inv = [5, 12, 8, 20, 15]
target = 20
found = False

for i in inv:
    if target == i:
        found = True
        break

if found == True:
        print("item mil gaya")

else:
     print("item nhi mila")