def cek_suhu(suhu):
    if suhu > 28:
        return "Panas"
    elif suhu >= 18 and suhu <= 28:
        return "Hangat"
    else:
        return "Dingin"
    
output = cek_suhu(18)
print(output)