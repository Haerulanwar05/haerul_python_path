# membuat sebuah program untuk mencari nilai tertinggi dari sebuah daftar nilai menggunakan for loop

nilai_siswa = [75, 88, 92, 85, 79, 95, 90]
nilai_tertingi = 0
for nilai in nilai_siswa:
    if nilai > nilai_tertingi:
        nilai_tertingi = nilai
print(f"Nilai Tertinggi yaitu: {nilai_tertingi}")
