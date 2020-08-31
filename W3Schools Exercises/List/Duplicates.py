def duplicates(lst):
    new_set = set(lst)
    new_list = list(new_set)
    return sorted(new_list)

result = duplicates([10,20,30,20,10,50,60,40,80,50,40])
print(result)