# kita membuat sebuah faktorial dengan module math
import math

try:
    angka = int(input("Masukan nilai angka: "))
except ValueError:
    print("inputan hanya angka selain angka salah!")
    quit()

hasil_faktorial = math.factorial(angka)
print(f"hasil faktorial dari {angka}! = {hasil_faktorial}")
 