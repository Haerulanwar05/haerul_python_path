'''
Rewrite Gross Pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
'''
print("Silahkan Mengecek Gaji kotor anda!")

jam = input("Masukan Total Jam kerja anda? ")

try:
    jam = float(jam)
except ValueError:
    print("anda tidak mengisi sebuah angka harap diulangi!")
    quit()
    

tarif = input("Masukan tarif per jam anda? ")

try:
    tarif = float(tarif)
except:
    print("anda tidak mengisi sebuah angka harap diulangi!")
    quit()  # Fungsi quit digunakan untuk keluar dari program jika terjadi error 


if jam > 40:
    upah_lembur = jam-40
    Hasil_upah_lembur = upah_lembur*tarif*1.5
    Gaji_Kotor = round(40*tarif+Hasil_upah_lembur,2)
    print(f"Gaji kotor anda sebesar : ${Gaji_Kotor}")
else:
    total_gaji = round(jam*tarif,2)
    print(f"Gaji kotor anda sebesar : ${total_gaji}")

