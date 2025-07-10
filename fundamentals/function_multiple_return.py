'''
bagaimana jika terdapat multiple return dari fungsi itu karena yang kita tahu return dalam fungsi merupakan sebuah akhir kode yang dibaca python jadi bagaimana jika ada beberapa return.
'''
# membuat fungsi format nama
def format_name(depan,belakang):
    if depan == "" or belakang == "":           #  kita menggunakan sebuah if apabila tidak tepernuhi maka akan melanjutkan kondisi yang bawah
        return "data ini tidak boleh kosong"
    f_depan = depan.title()
    f_belakang = belakang.title()
    return f"{f_depan},{f_belakang}"            # ini merupakan akhir kode yang dibaca python
   # kenapa harus menggunakan return karena kita akan memnaggil nya kembali dengan menggunakan variabel 

nama_depan = input("Masukan nama depan anda: ")
nama_belakang = input("Masukan nama belakang anda: ")

output = format_name(nama_depan,nama_belakang)
print(output)
