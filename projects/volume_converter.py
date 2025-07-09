'''
Definisikan sebuah fungsi yang mengonversi ons cair menjadi mililiter dan mencetak hasilnya ke konsol. Perhitungkan bahwa 1 ons cair sama dengan 29,57353 mililiter.
'''

def volume_converter(ons):
    result = ons * 29.57353
    print(f"{result} mililiter.")

volume_converter(10)