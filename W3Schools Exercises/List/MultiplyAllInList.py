my_List = [8,9,7,8,2,4]

def multiply(lst):
    result = 1
    if len(lst) !=0:
        for i in lst:
            result *= i
        return result
    else:
        return "Invalid Input"

print(multiply(my_List))