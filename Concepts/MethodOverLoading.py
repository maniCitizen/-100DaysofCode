class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a,b,c):
        
        s = None
        
        if a !=None and b !=None and c != None:
            s = a+b+c
        
        elif a !=None and b !=None:
            s = a+b
        
        elif a !=None:
            s = a
            
        return s
    
s1 =Student(58,69)
print(s1.sum(5,9,5))