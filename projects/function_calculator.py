def penjumlahan(n1,n2):
    return n1 + n2

def pengurangan(n1,n2):
    return n1 - n2

def perkalian(n1,n2):
    return n1 * n2

def pembagian(n1,n2):
    return n1 / n2

n1 = int(input("Masukan angka pertama: "))
n2 = int(input("Masukan angka kedua: "))
operasi = input("pilih operasi dari list ini (+,-,*,/): ")

if operasi == "+":
    hasil =  penjumlahan(n1,n2)
elif operasi == "-":
    hasil =  pengurangan(n1,n2)
elif operasi == "*":
    hasil =  perkalian(n1,n2)
else:
    hasil =  pembagian(n1,n2)

print (f"{n1} {operasi} {n2} = {hasil}")

