def modify_first_letter(word):
    final_word = ""
    for i in word[1:]:
        if i==word[0]:
           final_word += "$"
        else:
            final_word +=i
    return word[0] + final_word

print(modify_first_letter("restart"))

def change_char(word):
    char = word[0]
    new_word = word.replace(char, "$")
    final_word = char+new_word[1:]
    return final_word

print(change_char("restart"))