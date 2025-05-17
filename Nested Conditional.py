'''
nested conditionals merupakan sebuah kondisi dimana ketika nilai bernilai True atau False maka dalam kondisi tersebut terdapat kondisi lagi untuk mendapakan nilai atau True lagi
'''
# Contoh Syntax 
'''
kita membuat salah satu syarat agar bisa masuk karantina dengan kriteria seperti ini:
Suhu < 39
umur <= 70
'''
# Orang Pertama
suhu = int(input("Masukan Suhu pengecekan anda: "))
umur = int(input("Masukan umur anda: "))

if suhu < 39 and umur <= 70:
    print("Selamatt!,Anda memenuhi Syarat untuk Masuk")
else:
    print("Maaf anda tidak memenuhi syarat")
    Profesi = input("Masukan Profesi Anda: ")
    if Profesi == "Polisi" :
        print("Anda masuk ke pengawasan dalam zona!")
    elif Profesi == "Guru" :
        print("Anda masuk ke pengawasan dalam zona!")
    elif Profesi == "Dokter" :
        print("Anda masuk ke pengawasan dalam zona!")
    else :
        print("Maaf! kami sudah semaksimal mungkin untuk memperkuat keamanan syarat Karantina kami")

# Ini merupakan salah satu contoh Nested Conditional
# dalam eksekusi kondisi ini juga terdapat elif dimana ini digunakan untuk kondisi berantai seperti contoh diatas