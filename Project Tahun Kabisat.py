'''
Membuat sebuah project tahun kabisat dimana apabila bisa dibagi 4,100, dan 400 maka itu tahun kabisat
'''
tahun = int(input("Masukan tahun: "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("Ini Tahun Kabisat")
        else:
            print("Ini Bukan Tahun Kabisat")
    else:
        print("Ini Tahun Kabisat")
else:
    print("Ini Bukan Tahun Kabisat")