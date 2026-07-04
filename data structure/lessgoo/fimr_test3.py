player_badges = {"gamer_1": "gold", "gamer_2": "silver"}

chech_player = input("Enter your player name :- ")

if chech_player in player_badges:
    print(f"Yes, {chech_player} ko {player_badges[chech_player]}")

else:
    print("Yeh player list me nhi hai")
