def counter(lst):
    count = 0
    for i in lst:
        if len(i) >= 2:
            if i[0]==i[-1]:
                count += 1
    return count
            
result = counter(['abc', 'xyz', 'aba', '1221'])
print(result)