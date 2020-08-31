def lister(n, str):
    count = 0
    new_list = []
    strings = str.split(" ")
    for i in strings:
        if len(i)==n:
            count +=1
            new_list.append(i)
    return  count, new_list

result = lister(3, "The quick brown fox jumps over the lazy dog")
print(result)