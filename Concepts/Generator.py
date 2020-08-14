def topten():
    
    i = 1
    while i <=10:
        sq = i**2
        yield sq
        i +=1
        
values = topten()

print(values.next())

for i in values:
    print(i)


