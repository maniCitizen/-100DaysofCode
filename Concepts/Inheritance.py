class A:
    
    def feature1(self):
        print("The feature 1 is working")
        
    def feature2(self):
        print("The feature 2 is working")
        
class B(A):
    
    def feature3(self):
        print("The feautre 3 is working")
        
    def feature4(self):
        print("The feature 4 is working")
        
class C(A,B):
        
        def feature5(self):
            print("The feature 5 is working")
        
a1 = A()

b1 = B()

c1 = C()

c1.feature4()