# Implement a function that takes a list as a parameter and turn list items into their square.

def square_list(p_list):
    for index in range(len(p_list)):
        p_list[index] = p_list[index] * p_list[index]
    print(p_list)

custom_list = [1,2,3,4,5]
square_list(custom_list)
