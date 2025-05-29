'''
dalam project ini kita akan membuat sebuah perhitungan gaji kotor dengan tambahan upah lembur 1,5 dolar upah per jam nya apabila jam kerja diatas 40 jam kerja.
'''
try:
    print("Silahkan Mengecek Gaji kotor anda!")
    jam = float(input("Masukan Total Jam kerja anda? "))
    tarif = float(input("Masukan tarif per jam anda? "))
except:
    print("anda tidak mengisi sebuah angka harap diulangi!")

else:
    if jam > 40:
        upah_lembur = jam-40
        Hasil_upah_lembur = upah_lembur*tarif*1.5
        Gaji_Kotor = round(40*tarif+Hasil_upah_lembur,2)
        print(f"Gaji kotor anda sebesar : ${Gaji_Kotor}")
    else:
        total_gaji = round(jam*tarif,2)
        print(f"Gaji kotor anda sebesar : ${total_gaji}")
finally:
    print("Terimakasih Sudah Berkeja keras, Jaga kesehatan ya!")
