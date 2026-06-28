views = [120, 450, 890, 230, 670]
target = 890
index_found = -1

for i in range(len(views)):
   if views[i] == target:
        index_found = i
        break

if index_found != -1:
    print(f"index position hai {index_found}")
else:
    print("video nhi mila")