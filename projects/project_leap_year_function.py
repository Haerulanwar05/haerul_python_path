Year = int(input("Masukan Tahun: "))

def LapYear (year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Ini Tahun Kabisat")
            else:
                print("Ini Bukan Tahun Kabisat")
        else:
            print("Ini Tahun Kabisat")
    else:
        print("Ini Bukan Tahun Kabisat")

LapYear(Year)

# atau bisa juga seperti kita membuat filae baru yang mengandung function dan kita jadikan file tersebut sebagai modul

import module_func_leapyear as lp       # "as" digunakan untuk membuat alias atau mempersingkat module yang panjang

Tahun = int(input("Masukan Tahun: "))

lp.Lapyear(Tahun)

