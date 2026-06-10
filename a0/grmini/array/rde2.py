arr = [12, 44, 2, 45, 91]
bada = arr[0]
chota = arr[0]

for i in arr:
    if i > bada:
        bada = i
    if i < chota:
        chota = i

print(f"bada number : {bada}\nchota number : {chota}")
