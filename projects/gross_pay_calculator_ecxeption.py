'''
Rewrite Gross Pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
'''
try:
    quit(jam = (float(input("Masukan Total Jam kerja anda? "))))
    quit(tarif = (float(input("Masukan tarif per jam anda? "))))
except:
    print("anda tidak mengisi sebuah angka harap diulangi!")