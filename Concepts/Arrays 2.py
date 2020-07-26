from array import *

arr = array("i", [])

n = int(input("Enter the length of the array : "))

for i in range(n):
    x = int(input("Enter the next value : "))
    arr.append(x)
    
print("\n")
print("\n")

for j in arr:
    print(j)

val = int(input("Enter the value for search : "))

k = 0

for e in arr:
    if e == val:
        print(f"Value found at index {k}.")
        break
    k+=1
        