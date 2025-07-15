def Lapyear (year):
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
