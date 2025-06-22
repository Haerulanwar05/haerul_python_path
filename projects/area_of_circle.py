# menghitung luas lingkaran dengan module math
import math

try:
    radius = float(input("Masukan Radius: "))
except ValueError:
    print("inputan hanya angka selain angka salah!")
    quit()

area_circle = round(math.pi * math.pow(radius,2),2)
print(f"luas lingkaran tersebut adalah:{area_circle}")