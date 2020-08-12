# My solution

def add_string(text):
    length = len(text)
    
    if length <3:
        return text
    elif text[-3:]!="ing":
        return text+"ing"
    elif text[-3:]=="ing":
        return text+"ly"
    
print(add_string("abc"))
print(add_string("string"))

#W3schools Solution

def add_string(text):
    length  = len(text)
    
    if length >2:
        if text[-3:]=="ing":
            text += "ly" 
        else:
            text += "ing"
    
    return text

print(add_string("abc"))
print(add_string("string"))