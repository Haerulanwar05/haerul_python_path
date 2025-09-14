'''
dalam List terdapat beberapa operasi yang dapat digunakan contoh nya yaitu Slicing, Concatenate (+), Multiple (*), dan Exist Keywoard (in)
'''

# Slicing 
my_list = ["a","b","c","d"]
slicinglist = my_list[:2]   # kita ingin menampilkan bagian dari isi list tersebut yaitu ["a","b"]
print(slicinglist)

# Concatenate (+)
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)

# operasi mines dalam list akan menyebabkan error karena list tidak mendukung operasi -

# Multiple
print(list2 * 3)

# Exist Operasi 
'''
operasi ini mengeluarkan Output True atau False dalam list untuk menyatakan apa item dalam list tersebut ada atau tidak
'''
print(2 in list1)