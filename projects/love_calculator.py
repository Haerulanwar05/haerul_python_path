'''
Tulis program untuk menguji kecocokan antara dua orang.

Ambil nama kedua orang tersebut dan periksa berapa kali huruf dalam kata TRUE muncul. Kemudian periksa berapa kali huruf dalam kata LOVE muncul. Kemudian gabungkan angka-angka ini untuk membuat angka 2 digit.
For Love Scores less than 10 or greater than 85, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 70, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''
# Syntax
name1 = input("Masukan nama anda? ")
name2 = input("Masukan nama pasangan anda? ")
Nama_Gabungan = name1 + name2
Nama_Gabungan_Kecil = Nama_Gabungan.lower()

t = Nama_Gabungan_Kecil.count("t")
r = Nama_Gabungan_Kecil.count("r")
u = Nama_Gabungan_Kecil.count("u")
e = Nama_Gabungan_Kecil.count("e")

true = t + r + u + e

l = Nama_Gabungan_Kecil.count("l")
o = Nama_Gabungan_Kecil.count("o")
v = Nama_Gabungan_Kecil.count("v")
e = Nama_Gabungan_Kecil.count("e")

love = l + o + v + e

Love_Score = int(str(true)+str(love))
print(Love_Score)

if Love_Score < 10 or Love_Score > 85:
    print(f"Skor kamu adalah {Love_Score}, you go together like coke and mentos.")
elif 40 <= Love_Score >= 70:
    print(f"Skor kamu adalah {Love_Score}, you are alright together.")
else:
    print(f"Skor kamu adalah {Love_Score}.")

