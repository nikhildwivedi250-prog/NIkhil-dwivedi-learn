channels = {"techno_gamer": 55000000, "crazy_xyz": 38000000}

print(channels["crazy_xyz"])

channels["mythpat"] = 1600800
channels["ytkj"] = 15084700
channels["cobara"] = 10058
channels["mdad"] = 5000758


check_channel = input("Enter channel name : ")

if check_channel in channels:
    print("Haan ye channel list me hai ")
else:
    print("Ye channel list me nhi hai")