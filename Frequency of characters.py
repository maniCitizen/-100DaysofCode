def char_frequency(strings):
    dict = {}
    for i in strings:
        keys = dict.keys()
        if i in keys:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

n = char_frequency("google.com")
print(n)