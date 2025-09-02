'''
List merupakan sebuah data dimana befungsi untuk menyimpan suatu nilai atau jenis data lain di dalam nya
'''

angka = [10,20,30,40]       # ini merupakan sebuah data list int
names = ["Aji","Haerul","Mahesa","Iki"]      # ini merupakan sebuah jenis data string

# di list juga kita bisa mentranversal, dimana kita mengakses isi dalam list tersebut menggunakan looping

for nama in names:
    print(nama)

# atau kita juga bisa menggunakan sebuah index masih dalam konteks looping juga untuk mengakses isi dalam list

for index in range(len(names)):
    print(names[index])

# dan dalam angka kita bisa mengoperasikan sebuah operasi matematika sederhana

for index in range(len(angka)):
    angka[index] = angka[index] * 2 # disini kita membuat statemen dimana untuk mengupdate index lama ke baru
print(angka)

# error yang sering terjadi dalam list yaitu "index out of range"

negara = ["Indonesia","Malaysia","Amerika","Canada"]
banyak_negara = len(negara)
print(negara[banyak_negara])       # ini akan Error karena index yang keluar itu 4 sedangkan hanya 3 index dalam list dimana dalam menghitung index dimulai dari angka 0