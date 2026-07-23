try:
    amount = int(input("Enter your ammount : "))

    if amount <= 0:
        print("Invalid amount")
    else:
        print("Transaction successful")

except ValueError:
    print("Please enter only numbers ")