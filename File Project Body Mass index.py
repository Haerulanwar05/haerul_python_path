# Meminta data inputan dari User

Tinggi = float(input("Masukan Tinggi Anda dalam meter: "))
Berat = float(input("Masukan Berat badan anda dalam kg: "))

# Perhitungan 
bmi = round(Berat / Tinggi**2,2)

# Eksekusi Kondisi
if bmi < 18.5 :
    print(f"BMI anda adalah {bmi}, Anda kurus, makan yang banyak ya!!")
elif bmi < 25 :
    print(f"BMI anda adalah {bmi}, berat badan anda Normal, Pertahankan!!")
elif bmi < 30 : 
    print(f"BMI anda adalah {bmi}, Berat badan Anda lebih, tolong dikurangi!!")
else :
    print("Berat badan Anda Obesitas, Darurat segera dikurangi!!")

