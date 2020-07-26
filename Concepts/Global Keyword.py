a = 10

def something():
    global a
    a = 15
    print("In Function a :", a)
    
something()
print("Outside function a:", a)

a = 10
print(id(a))

def something():
    a = 15
    print("In function a:", a)
    x = globals()["a"]
    print(id(x))
    globals()["a"] = 15
    
    
something()
print("Outside function a:", a)