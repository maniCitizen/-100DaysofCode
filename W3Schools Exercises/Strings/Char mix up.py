# My solution

def char_mix_up(a,b):
    x = a[0:2]
    y = b[0:2]
    return y+a[2:]+" " + x+b[2:]

result = char_mix_up("abc", "xyz")
print(result)

# W3resource solution
def char_mix_up(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    
    return new_a + " " + new_b

char_mix_up("abc", "xyz")