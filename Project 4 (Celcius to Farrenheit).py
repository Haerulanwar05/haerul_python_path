'''
Instruction
Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature. Formula : (°C × 9/5) + 32 = °F
'''
# syntax
Celcius = float(input("Masukan Celcius: "))
Hasil = (Celcius*9/5)+32
print(f"{Celcius} Celcius = {Hasil} Fahrenheit")