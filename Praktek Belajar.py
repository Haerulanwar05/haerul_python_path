'''
Membuat sebuah konsep tentang Kriteria kost an yang cocok untuk mahasiswa Universitas Trilogi
dimana beberapa syarat sebagai berikut harus terpenuhi yaitu :
1. Mahasiswa yang belum berkerja mendapat Kriteria Kost an tipe "C"
2. Mahasiswa yang mempunyai pekerjaan dibawah 1 juta gaji perbulannya mendapat kriteria Kost an tipe "B"
3. Mahasiswa yang mempunyai pekerjaan diatas 1 juta gaji perbulannya mendapat kriteria kost an tipe "A"
terdapa beberapa tambahan apabila mahasiswa dari 3 kriteria ini menyesuaikan lagi untuk tipe kost nya dimana:
- apabila mahasiswa tersebut mendapat beasiswa diatas 5 juta/bulan nya maka dia mendapat kriteria "A"
- apabila mahasiswa tersebut mendapat beasiswa dibawah 5 juta/bulan nya maka dia mendapat kriteria "B"
'''
# Syntax 
print("Selamat datang di pengecekan kriteria kost untuk mahasiswa!")
try:
    Mahasiswa = input("Masukan Nama anda? ")
    Status = input("Masukan Status anda? ")
    Pendapatan = int(input("Masukan nominal pendapatan anda? "))
except:
    print("maaf yang anda masukan sebuah tipe data yang tidak ditemukan")

else: 
    if Pendapatan == 0:
        Beasiswa = input("apakah anda mendapatkan beasiswa? (Y/N) ")
        if Beasiswa == "Y":
            Nominal_Beasiswa = int(input("masukan nominal beasiswa anda? "))
            if Nominal_Beasiswa < 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'B'")
            elif Nominal_Beasiswa > 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'A'")
            else:
                pass
        else:
            print(f"Halo {Mahasiswa}, Status anda adalah {Status}, jadi anda mendapatkan kriteria kost an tipe 'C'")
    elif Pendapatan <= 1000000:
        Beasiswa = input("apakah anda mendapatkan beasiswa? (Y/N) ")
        if Beasiswa == "Y":
            Nominal_Beasiswa = int(input("masukan nominal beasiswa anda? "))
            if Nominal_Beasiswa < 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'B'")
            elif Nominal_Beasiswa > 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'A'")
            else:
                pass
        else:
            print(f"Halo {Mahasiswa}, Status anda adalah {Status}, jadi anda mendapatkan kriteria kost an tipe 'B'")
    else:
        Beasiswa = input("apakah anda mendapatkan beasiswa? (Y/N) ")
        if Beasiswa == "Y":
            Nominal_Beasiswa = int(input("masukan nominal beasiswa anda? "))
            if Nominal_Beasiswa < 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'B'")
            elif Nominal_Beasiswa > 5000000:
                print(f"Halo {Mahasiswa}, Status anda adalah {Status}, dan anda mendapatkan Beasiswa jadi anda mendapatkan kriteria kost an tipe 'A'")
            else:
                pass
        else:
            print(f"Halo {Mahasiswa}, Status anda adalah {Status}, jadi anda mendapatkan kriteria kost an tipe 'A'")

finally:
    print("Terimakasih sudah melakukan pengecekan kriteria kost untuk mahasiswa!")
 


