import math
import random

lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))
chances = int(math.log(upper - lower +1,2))

print(f"\t\n You've only {chances} chances to guess the integer!\n\t")

guess_number = random.randint(lower,upper)
count = 0
while count < chances:
    count += 1
    input_number = int(input("Enter a guess number: "))
    if input_number == guess_number:
        print(f"Congratulations you dit it in {count} try")
        break
    elif input_number > guess_number:
        print("You Guessed too high!")
    elif input_number < guess_number:
        print("You guessed too small!")

print(f"\nThe number is {guess_number}\n\tBetter Luck Next time")