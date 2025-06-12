'''
Instruction
Write a program which calculates trip cost for a user.
1. Create a greeting for your program.
2. Ask the user for number of days.
3. Ask the user for hotel price.
4. Ask the user for flight price.
5. Ask the user for rental car price.
6. Ask for other expenses.
Combine all expenses together and print with 2 digits after decimal places.
'''
# Syntax
print("Welcome to the Trip Cost Calculator!")
hari = int(input("Berapa Hari Anda ingin Menetap?\n"))
Harga_Hotel = float(input("Berapa Harga Hotel Per Malam?\n"))
Harga_Tiket_Pesawat = float(input("Berapa Harga Tiket Pesawat?\n"))
Sewa_Mobil = float(input("Berapa Harga Rental Mobil?\n"))
Biaya_lain = float(input("Masukan Biaya Lain-lain (Jika tidak ada Masukan 0)?\n"))
Total_Biaya = (hari*Harga_Hotel)+Harga_Tiket_Pesawat+(hari*Sewa_Mobil)+Biaya_lain
print(f"total biaya = {round(Total_Biaya,2)}")