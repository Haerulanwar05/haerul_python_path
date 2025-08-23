# Parsing String

data = 'From example.email@edu.co.uk Sat Sep 5 09:14:16 2021'

at_index = data.find('@')
print(at_index)
space_after_at = data.find(' ', at_index)
print(space_after_at)
domain = data[at_index+1 : space_after_at]
print(domain)

# slicing string dengan fuungsi built in
my_string = "I Love learning Python"
output = my_string.split()
'''
pada dasarnya untuk memisahkan sebuah string dalam fungsi built in tersebut kita harus mencari parameter untuk mengukur sebuah string tersebut dari fungsi built in dan berapa maksimal split nya semacam (parameter,maksplit)
'''
print(output)

# bagaimana dengan menggabungkan nya kembali?
'''
kita bisa menggunakan syntax join dimana tujuan nya yaitu menggabungkan string yang di split dalam list
dan tentu menggunakan parameter beda nya dia harus meminta parameter itu senditi seperti ' '.join(target)
'''
join_back = " ".join(output)
print(join_back)


custom_string = 'X-MAPDS-Confidence:0.8475' 
index_col = custom_string.find(":")
number = custom_string[index_col + 1: ]
number = float(number)
print(number)