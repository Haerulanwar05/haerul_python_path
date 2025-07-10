'''
disini kita akan membuat sebuah program dimana program ini memberi tahu kita berapa kaleng cat yang dibutuhkan untuk mengecat suatu dinding, jika 1 kaleng bisa mengcover 4 dinding maka kita harus membuat fungsi dimana dalam fungsi tersebut memberi kita ukuran panjang dan lebar suatu dinding dan kita menghitung area luas dinding dan menghitung berapa kaleng cat yang dibutuhkan berdasarkan luas dinding tersebut
'''
import math

def perhitungan_kaleng_cat(panjang,lebar,cover):
    luas_area = panjang * lebar 
    kaleng_dibutuhkan = math.ceil(luas_area / cover)   # kita menggunakan ceil jadi kita harus import module math
    print(f"Kaleng Cat yang dibutuhkan adalah sebanyak {kaleng_dibutuhkan} kaleng.")

panjang = int(input("Masukan panjang dinding: "))           # ini merupakan penginputan dari user
lebar = int(input("Masukan lebar dinding: "))               # ini merupakan penginputan dari user

perhitungan_kaleng_cat(panjang,lebar,4)

