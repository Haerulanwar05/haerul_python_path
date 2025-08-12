'''
String Traversal merupakan cara mengakses seluruh index yang berada di dalam string dengan menggunakan For loop dan While loop
'''

# Mencotohkan dengan While loop karena for loop sangat sederhana
fruit = "banana"

index = 0                   # membuat sebuah variabel dengan value 0 agar dijadikan parameter untuk While loop
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1


# backward traversal

string = input("Enter a string: ")

length = -1 * len(string)
indexs = -1

while indexs >= length:
    letters = string [indexs]
    print(letters)
    indexs -= 1


