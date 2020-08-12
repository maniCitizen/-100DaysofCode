#My solution

def exchange(str):
    first_char = str[0]
    last_char = str[-1]
    remaining_word = str[1:-1]
    first_char,last_char = last_char,first_char
    return first_char+remaining_word+last_char

result = exchange("Python")
print(result)

#W3Resource Solution

def changestring(str):
    return str[-1:]+str[1:-1]+str[:1]
    
changestring("Python")
