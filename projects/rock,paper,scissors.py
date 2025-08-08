import random as rd

def select_computer_actions():
    possible_action = ["rock", "paper", "scissors"]
    computer_action = rd.choice(possible_action)
    return computer_action

def determine_winner(p_computer_action, p_user_action):
    if p_user_action == p_computer_action:
        print(f"Both players selected {p_user_action}. It's a tie!")
    elif p_user_action == "rock":
        if p_computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif p_user_action == "scissors":
        if p_computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif p_user_action == "paper":
        if p_computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")


while True:
    input_user = input("Enter a choice (rock, paper, scissors): ")
    input_computer = select_computer_actions()
    print(f"\nYou chose {input_user}, computer chose {input_computer}.\n")
    winner = determine_winner(input_computer,input_user)
    asking = input("Play Again (Y/N)? ")
    if asking != "Y":
        break




    

    


    




