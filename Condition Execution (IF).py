'''
dalam Eksekusi kondisi terdapat 3 jenis yaitu IF,ELIF,ElSE dalam pengeksekusian nya program membaca suatu kondisi 
dari program tersebut apabila salah satu kondisi nya terpenuhi maka program akan akan membaca atau mengeksekusi kondisi yang
terpenuhi.
'''
# Syntax
'''
kita membuat salah satu syarat agar bisa masuk karantina dengan kriteria seperti ini:
Suhu < 39
umur <= 70
'''
# Orang Pertama
suhu = int(input("Masukan Suhu pengecekan anda: "))
umur = int(input("Masukan umur anda: "))

if suhu < 39 and umur <= 70:
    print("Selamatt!,Anda memenuhi Syarat untuk Masuk")
else:
    print("Maaf anda tidak memenuhi syarat")

# dalam penulisan kode sebuah kondisi indentasi sangat harus diperhatikan agar tidak error dalam python itu tersebut 
# AND sendiri dalam program beberapa kondisi yang harus terpenuhi semuanya
# OR sendiri beberapa kondisi yang dimana tidak harus semuanya terpenuhi jika salah satu nya terpenuhi maka nilai nya akan True
# Pass sendiri merupakan sebuah perintah dimana jika nilai benar maka dia tidak mengesekusi apapun
