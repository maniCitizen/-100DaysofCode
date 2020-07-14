from array import *

vals = array("i", [1,2,5,8,6])

print(vals[4])

for i in range(5):
    print(vals[i])
    
for i in range(len(vals)):
    print(vals[i])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)
    
vals = array("u", ["a", "e", "i"])

for i in vals:
    print(i)