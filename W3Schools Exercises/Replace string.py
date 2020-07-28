def replace_string(sentence):
    not_word = sentence.find("not")
    poor_word = sentence.find("poor")
    
    if not_word==-1 or poor_word==-1:
        result = sentence 
    else:
        if not_word<poor_word:
            result = sentence[:not_word]+"good"
    return result

result1 = replace_string("The lyrics is not that poor!")
result2 = replace_string("The lyrics is poor!")

print(result1)
print(result2)
