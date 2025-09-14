'''
dalam list di python kita bisa mengetahui method apa saja dalam list menggunakan fungsi dir
'''
animals = ['kucing','ayam','singa','burung','anjing','ular','beruang','anjing']
print(dir(animals))

#output
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# Index
'''
method index dalam list mengetahui index item dalam list yang kita inginkan dalam perintah index terdapat beberapa struktur yaitu (object,start,stop)
'''
index_list = animals.index('anjing')
print(index_list)

# bagaimana jika dalam list itu terdapat index yang sama?
index_list = animals.index('anjing', 5) # kita ingin mencari item yang sama selain yang pertama jadi kita mulai dari index setelah nya
print(index_list)


# Append
'''
append merupakan method untuk menambah item di list dan diletakkan selalu di akhir index serta hanya bisa object tunggal saja
'''
animals.append('kura-kura')
print(animals)

# Extend
'''
Extend merupakan method yang sama tetapi bisa menambahkan beberapa object
'''
animals2 = ['rubah','tupai']
animals.extend(animals2)
print(animals)

# Insert
'''
insert merupakan method yang sama dengan append tetapi kita bisa bebas ingin menaruh object di index mana
'''
animals.insert(4, 'elang')
print(animals)

# Remove
'''
method ini menghapus sebuah object dalam list, apabila dalam list tersebut terdapat 2 object yang sama maka index yang lebih dahulu akan dihapus
'''
animals.remove('anjing')
print(animals)

# Count
'''
count method dalam list yaitu fungsi nya menghitung terdaoat berapa object dalam list tersebut
'''
print(animals.count('kura-kura'))

# Pop
'''
Pop Method dalam list yaitu menghapus object dalam item dan me return object itu sendiri
'''
item = animals.pop(3) # dalam pop untuk menghapus kita harus memberikan sebuah index dari object nya 
print(item)
print(animals)

# Reverse 
'''
reverse method dalam list yaitu membalikan sebuah index dimana tampilan akan diurutkan dari index pertama ke terakhir
'''
animals.reverse()
print(animals)

# ini tidak bisa di tambahkan dalam variabel baru maka hasil nya akan menjadi none.

# Sort
'''
sort method merupakan sebuah fungsi dalam list dimana merapihkan object dalam list berdasarkan abjad atau jika angka dari terkecil ke terbesar by default
'''
angka = [1,3,4,2,6,5,7,10,9,8]
angka.sort()    # ini sort by default
print(angka)
angka.sort(reverse=True)    # ini berdasarkan reverse dari terbesar ke terkecil
print(angka)

# Copy
'''
copy method merupakan menduplikat sebuah list berserta object nya tanpa terhubung satu sama lain
'''
new_animals = animals.copy()
new_animals.append('gajah')
print(animals)
print(new_animals)

# jika kita membuat nya seperti ini
# new_animals = animals , maka aan terhubung jika kita memodifikasi new_animals maka animals nya juga ikut berubah

# Clear
'''
clear method merupakan sebuah method dalam list dimana dia menghapus seluruh object dalam list dan hanya mnyisakan  list nya saja.
'''
animals.clear()
print(animals)