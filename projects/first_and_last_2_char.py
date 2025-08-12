def first_last_characters(word):
    if len(word) < 2:
        return " "
    first_2_char = word[0:2]
    last_2_char = word[-2:]
    result = first_2_char + last_2_char
    return result

print(first_last_characters("Haerul"))
    