def angka_3_besar(num1,num2,num3):
    return max(num1,num2,num3)

num1 = int(input("masukan angka ke-1: "))
num2 = int(input("masukan angka ke-2: "))
num3 = int(input("masukan angka ke-3: "))

output = angka_3_besar(num1,num2,num3)
print(output)