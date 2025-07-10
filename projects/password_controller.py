'''
Buat fungsi yang menggunakan string password sebagai parameter dan memeriksa panjang kata sandi. Jika panjangnya lebih dari 8 karakter, fungsi akan mengembalikan True, jika tidak, akan mengembalikan False.
'''
def password_controller(password):
    ''' ini merupakan sebuah fungsi password untuk mengecek panjang 
    karakter password
    '''
    panjang_password = len(password)
    if panjang_password > 8:
        return True
    else:
        return False

output = password_controller("123")
print(output)