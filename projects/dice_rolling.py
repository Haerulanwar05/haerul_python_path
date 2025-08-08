import random as rd

while True:
    Dice1 = rd.randint(1,6)
    print(f"Dice1:{Dice1}")
    Dice2 = rd.randint(1,6)
    print(f"Dice2:{Dice2}")

    decision = input("Roll the dice again? (Y/N)")
    if decision == "Y":
        pass
    else:
        break

    
    