a = 0
a = a + 1
# Kode ini mendeklarasikan variabel a dengan nilai awal 0,
# lalu menambahkannya dengan 1 sehingga nilai a menjadi 1.

# b = b + 1
# Kode ini akan menghasilkan error karena variabel b belum dideklarasikan sebelumnya.
# Untuk menghindari error, kita harus mendeklarasikan b terlebih dahulu.
# Contoh yang benar:
b = 0
b = b + 1
# Kode ini mendeklarasikan variabel b dengan nilai awal 0,
# jadi kita bisa mengupdate variabel ini karena variabel b sudah ada sebelumnya.

# Contoh penggunaan loop untuk mengupdate variabel dalam Python
sayuran = ['bayam', 'kangkung', 'sawi']
for sayur in sayuran:           # Membuat loop untuk setiap sayur dalam list sayuran
    s = s + sayuran # Ini akan menghasilkan error karena variabel s belum dideklarasikan.
    print(sayur)            

# contoh lain mengupdate variabel dalam loop yang benar
angka_list = [1, 2, 3]
c = 0  # Mendeklarasikan variabel c sebelum digunakan
for angka in angka_list:          # Membuat loop untuk setiap angka dalam list angka_list
    c = c + angka  # Mengupdate variabel c dengan menambahkan angka saat ini
    # Ini akan menambahkan setiap angka dalam angka_list ke c 
    print(c)  # Menampilkan nilai c yang telah diupdate



