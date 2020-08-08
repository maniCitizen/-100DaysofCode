class Computer:
    
    def __init__(self):
        self.name = "Tamil"
        self.age = 30
        
    def update(self):
        self.age = 30
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
         
c1 = Computer()
c2 = Computer()
c2.age = 35

if c1.compare(c2):
    print("They are same.")
else:
    print("They are not same.")

print(c1.name)
print(c2.age)
