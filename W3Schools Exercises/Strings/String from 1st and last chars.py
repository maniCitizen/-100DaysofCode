def return_word(word):
    if len(word) < 2:
        return None
    else:
        position = len(word)-2
        new_word = word[:2]+word[position:]
        return new_word
    
print(return_word("w3resource"))
print(return_word("w3"))
print(return_word("w"))