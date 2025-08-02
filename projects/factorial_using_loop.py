def factorial (p_num):
    factorial = 1           # kita memambahkan sebuah variabel dengan 1 untuk perkalian
    if p_num < 0:
        return "angka negatif tidak ada dalam faktorial"
    elif p_num == 0:
        return "faktorial dari angka 0 adalah 1"
    else:
        for num in range (1, p_num + 1):
            factorial = factorial * num
        return f"faktorial dari {p_num} adalah {factorial}"
print(factorial(-3))
