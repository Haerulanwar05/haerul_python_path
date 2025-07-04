import random

input_tebakan = int(input("Masukan angka? "))
angka_random = random.randint (1,10)

if input_tebakan == angka_random :
    print(f"tebakan nya yaitu {angka_random} dan anda menebak {input_tebakan} maka anda beruntung")
else:
    print(f"tebakan nya yaitu {angka_random} dan anda menebak {input_tebakan} anda kurang beruntung :(")

    

