word = input("Please enter a word : ")
print(len(word))

def count_words(text):
    chars = 0
    for i in text:
        chars +=1
    return chars

print(count_words("Tamilarasan"))