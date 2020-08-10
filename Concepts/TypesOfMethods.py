class Student:
    
    school = "Telusko"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
    @classmethod
    def get_school_name(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is a statement from the static method.")
    
    
stud1 = Student(68,35,56)
stud2 = Student(23,12,89)


print(stud1.avg())
print(stud2.avg())

print(stud1.get_m1())
print(stud2.get_m1())

print(Student.get_school_name())

Student.info()



