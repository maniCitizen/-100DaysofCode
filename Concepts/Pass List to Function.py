def count(lst):
    even = 0
    odd = 0    
    for i in lst:
        if i%2==0:
           even+=1
        else:
            odd+=1
    return odd,even

list1 = [24,69,87,25,74,64,24,20]
odd,even = count(list1) 
print(f"Even : {even} and Odd : {odd}")