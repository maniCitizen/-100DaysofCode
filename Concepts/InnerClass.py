class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollno)
        
    class Laptop:
        
        def __init__(self):
                self.brand = "HP"
                self.cpu = "i5"
                self.ram = 4
                
        def show(self):
            print(self.brand, self.cpu, self.ram)
        
s1 = Student("Tamil", 2)
s2 = Student("Navin", 5)

s1.show()
s2.show()
s1.lap.show()
