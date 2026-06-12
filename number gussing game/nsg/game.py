import random

def start_game():
    print("=== Welcome to the gussing game ===")
    print("Maine 1 se 50 ke bich ek number socha hai kya tum bata sakate ho")

    computer_number = random.randint(1, 50)
    attempts = 0

    while True:
        user_guess = int(input("\nApana guess number dalo: "))
        attempts +=1
        

        if user_guess == computer_number:
            print(f"badhai ho aapane shai guess kiya hai.")
            print(f"total attempt : {attempts}")
            break

        elif user_guess < computer_number:
            print("Thoda bada number spcho")
        else:
            print("Thoda chota number socho")

        if attempts == 5:
            print("\nGame over aapki life line samapt hui")
            print(f"Sahi number {computer_number} tha")
            break

start_game()