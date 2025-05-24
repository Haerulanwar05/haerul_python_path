# Burger Order
'''
Burger Order
Write a program that calculates final bill Burger Order Price based on a user's choice.

Price List.
Mini Burger (M) : $5
Normal Burger (N): $8
Large Burger (L) : $10
Add Mushroom : For Mini and Normal = $1, For Large = $2
Extra Cheese : $1
'''
# Syntax
print("Selamat datang di Burger Order!") 
print("Berikut Daftar harga Burger:\nMini : $5\nNormal : $8\nLarge : $10")
Size = input("Masukan Size Burger(M,N,L)? ")
Harga = 0
if Size == "M":
    Harga = 5
elif Size == "N":
    Harga = 8
elif Size == "L":
    Harga = 10
else :
    print("Input Tidak ditemukan")
add_Mushroom  = input("Apakah ingin menambahkan Jamur (Y/N)? ")
if add_Mushroom == "Y":
    print("Berikut List ukuran Jamur")
    print("Mini & Normal: $1\nLarge : $2")
    Size_Mushroom = input("Masukan Size Jamur? ")
    if Size_Mushroom == "Mini":
        Harga += 1
    elif Size_Mushroom == "Normal":
        Harga += 1
    elif Size_Mushroom == "Large":
        Harga += 2
    else :
        print("Input Tidak ditemukan")
elif add_Mushroom == "N" :
    pass
else :
    print("Input Tidak ditemukan")
Penambahan_keju = input("Apakah ingin menambahkan keju (Y/N)? ")
if Penambahan_keju == "Y":
    Harga += 1
    print("Penambahan Keju dikenai Biaya $1")
elif Penambahan_keju == "N":
    pass
else : 
    print("Input Tidak ditemukan")
print (f"Pesanan anda dengan ukuran {Size} sebesar : ${Harga}")

    