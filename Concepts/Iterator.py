class TopTen:
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def next(self):
        
        if self.num <=10:
            val = self.num
            self.num += 1
        
        else:
            raise StopIteration
        
        return val
    
t1 = TopTen()
print(next(t1))

for i in t1:
    print(i)

    