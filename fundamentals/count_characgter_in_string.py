def count_letter(word, letter):
    hasil_count = 0
    for letters in word:
        if letters == letter:
            hasil_count += 1
    return hasil_count

print(count_letter("akusukaambalabu","u"))
        

        
    
            