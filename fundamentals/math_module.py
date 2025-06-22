# jika kita ingin mengakses sebuah modul math maka kita harus mengimport module nya
import math
print(math) # untuk mengetahui apa math itu

print(math.ceil(4.2)) # penggunaan salah satu functions dalam module math 

print(math.trunc(5.7)) # contoh penggunaan functions lain dalam modul math

# kita juga bisa membuat module tersendiri contoh nya dibawah ini:
import my_module # mengimport module sendiri
print(my_module.sapa("Haerul")) # penggunaan sebuah func sendiri/UDF dalam module yang kita buat