try:
    nilai = float(input("Masukan Nilai:\n"))
except ValueError:
    print("nilai seharusnya adalah angka, selain angka salah!")
    quit()

if nilai >= 0.0 and nilai <= 1.0:
    if nilai >= 0.9:
        print("A")
    elif nilai >= 0.8:
        print("B")
    elif nilai >= 0.7:
        print("C")
    elif nilai >= 0.6:
        print("D")
    else:
        print("f")
else:
    print("bad score")