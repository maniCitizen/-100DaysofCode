def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
person("Tamil", age = 28, city = "Bangalore", mob = 9823654789)