def comparer(list1, list2):
    for x in list1:
        for y in list2:
            if x==y:
                result = True
    
    return result

result = comparer([1,2,3,4,5], [5,6,7,8,9])
print(result)