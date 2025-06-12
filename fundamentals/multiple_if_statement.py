'''
Multiple IF Statement merupakan sebuah if dimana setelah kondisi if sebelumya sudah terpenuhi dan ingin mengeksekusi atau memenuhi kondisi lain dalam sebuah program.
'''
# Syntax
print("Welcome to the Mortage Calculator!")
salary = int(input("What is you salary? "))
rate = 0

if salary >= 2000:
    print("You are Eligible for mortage!")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        rate = 4
        print("Interest rate: 4%")
    elif credit_score > 750:
        rate = 6
        print("Interest rate: 6%")
    else :
        rate = 8
        print("Interest rate: 8%")
    disability = (input("Do you have any disability (Y or N)? "))
    if disability == "Y":
        rate -= 2
    print(f"Your Final rate is {rate}%")   
else:
    print("Sorry, you are not eligible!")

# dalam syntax tersebut terdapat IF,Nested if, and multiple if.