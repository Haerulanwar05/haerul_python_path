import random as rd

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

letters_input = int(input("How many letters do you want in your password? "))
numbers_input = int(input("How many numbers do you want in your password? "))
symbols_input = int(input("How many symbols do you want in your password? "))

result_password = ""


for letter in range(1, letters_input + 1):
    result_password += rd.choice(letters)

for num in range(1, numbers_input + 1):
    result_password += rd.choice(nums)

for symbol in range(1, symbols_input + 1):
    result_password += rd.choice(symbols)

print(f"Your password is: {result_password}")

password_list = list(result_password)
rd.shuffle(password_list)

complex_password = ""

for password in password_list:
    complex_password += str(password)

print(f"Your advance password is: {complex_password}")
