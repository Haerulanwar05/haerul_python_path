
def perhitungan_pembayaran(jam,tarif):
        hasil = round(jam*tarif,2)    
        return f"Bayar : {hasil}"

def cek_data(data):
    try:
        data = float(data)
        return data
    except ValueError:
        print("Error, yang anda masukan bukan sebuah data float")
        quit()

Jam = input("Masukan Jam kerja Anda: ")
Jam = cek_data(Jam)
Tarif = input("Masukan Tarif Anda: ")
Tarif = cek_data(Tarif)     

output = perhitungan_pembayaran(Jam,Tarif)
print(output)

    

