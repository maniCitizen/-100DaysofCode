a = 5
b = 2

try:
    print(a/b)
    print("The resource is open.")
    n = int(input("Please enter a number : "))
    
    
except ZeroDivisionError as e:
    print("You cannot divide a num by zero.")
    
except ValueError as e:
    print("Invalid Input")
    
except Exception as e:
    print("Something went wrong.")
    
finally:
    print("The resource is closed.")
    