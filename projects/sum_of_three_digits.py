num = input("Enter an integer number: ")

index = 0
length = len(num)
sum_of_digits = 0
while index < length:
    number = int(num[index])        # cara panjang
    sum_of_digits += number
    index += 1
print(sum_of_digits)


penjumlahan = 0
for angka in num:
    penjumlahan += int(angka)       # cara pendek

print(penjumlahan)
