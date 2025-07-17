Buah = ["pisang", "Jeruk", "Mangga"]

print(Buah[0]) # Output: pisang

print(Buah[-1]) # Output: Mangga

Buah.append("Apel") # Menambahkan Apel ke dalam list
print(Buah) # Output : ["pisang", "Jeruk", "Mangga", "Apel"]

# Kita juga bisa menukar sebuah item dalam list contohnya di bawah ini:
Buah[1] = "Jeruk Bali" # Mengganti 'Jeruk' dengan 'Jeruk Bali'
print(Buah) # Output: ["pisang", "Jeruk Bali", "Mangga", "Apel"]