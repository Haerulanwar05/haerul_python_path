sayuran = ['bayam', 'kangkung', 'sawi']

for sayur in sayuran:           # Membuat loop untuk setiap sayur dalam list sayuran
    print(sayur)            # Menampilkan nama sayur dalam loop, dia akan menampilkan setiap item dalam list sayuran satu per satu

buah_list = ["apel", "jeruk", "mangga"]

for buah in buah_list:          # Membuat loop untuk setiap buah dalam list buah_list
    print(buah)            
    print(buah + " pie")    # Menampilkan nama buah dan menambahkan " pie" pada setiap buah dalam loop, dan akan menampilkan setiap item dalam list buah_list satu per satu
    print(buah_list) 
    '''
    Menampilkan seluruh list buah_list pada setiap iterasi, ini akan menampilkan list lengkap setiap kali loop berjalan, dia akan menampilkan list buah sebanyak 3 kali sesuai jumlah item dalam list buah_list,
    3 syntax ini akan dieksekusi sesuai dengan jumlah item nya jika item "apel" maka 3 syntax ini akan fokus pada item apel tersebut dan akan menampilkan "apel", "apel pie", dan ["apel", "jeruk", "mangga"] pada iterasi pertama, begitu juga dengan item lainnya.
    '''