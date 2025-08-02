def check_for_float (p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError,TypeError):
        print("mohon masukan sebuah angka")
        return False

input1 = input("Masukan sebuah angka: ")
if input1 == "done":
    quit()

number = check_for_float(input1)
if not number:
    print("yang diisi pertama harus angka untuk melanjutkan....")
    quit()

terbesar = number
terkecil = number

while True:
    input1 = input("Masukan sebuah angka: ")
    if input1 == "done":
        break
    number = check_for_float(input1)
    if number > terbesar:
        terbesar = number
    if number < terkecil:
        terkecil = number

print(f"Maximum number: {terbesar}, Minimum number {terkecil}")

    

