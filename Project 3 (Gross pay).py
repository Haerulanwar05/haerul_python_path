'''
Instruction
Write a program to prompt the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.
'''
# syntax
Jam = float(input("Masukan Jam: "))
tarif = float(input("Masukan Tarif: "))
Bayaran_Kotor = round(Jam*tarif,2) 
print(f"Bayar : {Bayaran_Kotor}")


