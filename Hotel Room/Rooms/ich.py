menu = {
    "1_star": 500,
    "2_star": 1500,
    "3_star": 5000,
    "4_star": 8000,
    "5_star": 15000
}

print("----Welcome to Hasina Hotel Room----")
print("1_star: 500\n2_star: 1500\n3_star: 5000\n4_star: 8000\n5_star: 15000")



room = input("Aap kaunsa room lena chahate hai :- ")

if room == "1_star":
    print("Room me aapko bistar towel and  milegi ")

elif room == "2_star":
    print("Room me aapko bistar towel tea induction  washroom  milegi ")

elif room == "3_star":
    print("Room me aapko bistar towel tea induction AC / heater washroom  milegi ")

elif room == "3_star":
    print("Luxuriouse Room milegi ")

elif room == "5_star":
    print("Aapko luxury Room ke sath sath har shuvidha provaid karayi jayegi")

else:
    print("Room ka name dale")


print("thanks for visit our Hotel Room")