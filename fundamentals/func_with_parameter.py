# function with input

def greeting (name) :   # dalam  function ini hanya membuat 1 parameter yaitu "name"
    print(f"halo selamat pagi {name}!")
    print(f"bagaimana kabar anda {name}?")

# kita akan membuat function dengan 2 parameter
def greet_with_city(a,b):   # dalam hal ini terdapat 2 parameter dimana a untuk nama dan b untuk kota
    print(f"Halo Selamat Pagi {a}!")
    print(f"Anda berasal dari kota {b}")

greet_with_city("jakarta","Haerul")   # dalam hal ini kita harus memperhatikan penginputan data yang ingin dmasukan

# karena dalam python terdapat positional argumen dimana kita harus sesuaikan dengan variabel yang ingin kita isi
# contoh output :
''' 
Halo Selamat Pagi jakarta!               
Anda berasal dari kota Haerul
'''
# dia akan terbalik outputnya karena menempatkan data yang kita masuki secara salah.
# harusnya begini yang benar:

greet_with_city("Haerul","jakarta")

# dalam func ini sebenarnya kita bisa membuat lebih dari 2 atau banyak parameter yang digunakan dalam pembuatan kode nya
'''
dalam function ini juga terdapat yang namanya keyword argument dimana kita menandakan data apa yang harus kita isi lalu kedepannya sehingga kita menaruh nya di posisi yang salah seharusnya tidak tertukar
'''

def greeting_cityKA(name, city):     
    print(f"halo selamat pagi {name}!")                     
    print(f"bagaiman cuaca di kota {city}?")

greeting_cityKA(city="Jakarta",name="Haerul")              # kita menandakan parameter ini sesuai apa yang ingin kita isi jadi jika kita lupa posisi nya dan tertukar maka tidak akan logic error


# membuat fungsi format nama
def format_name(depan,belakang):
    f_depan = depan.title()
    f_belakang = belakang.title()
    return f"{f_depan},{f_belakang}"   # kenapa harus menggunakan return karena kita akan memnaggil nya kembali dengan menggunakan variabel 

output = format_name("haerul","anwar")
print(output)

# membuat fungsi concatenate string
def concatenate(a,b):
    f_concatenate = a + b
    return f_concatenate

output_concatenate = concatenate("Face","Book")
print(output_concatenate)