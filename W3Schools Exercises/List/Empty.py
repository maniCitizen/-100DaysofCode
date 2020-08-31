#My Code

def empty(lst):
    result = ""
    if len(lst)==0:
        result = "List is empty."
    else:
        result = "List is not empty."
    
    return result

result = empty([])
print(result)

# W3Resource method

l = []
if not l:
    print("The list is empty.")