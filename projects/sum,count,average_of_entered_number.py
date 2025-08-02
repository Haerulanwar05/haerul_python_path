def check_of_float (p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError,TypeError):
        print("mohon masukan sebuah angka")
        return False

count = 0
sum = 0.0
average = 0.0

while True:
    input_numbers = input("masukan sebuah angka: ")
    if input_numbers == "done":
        break

    number = check_of_float (input_numbers)
    if not number:
        continue
        
    count += 1
    sum += number
if count != 0:
    average = sum/count
print(sum, count, average)

