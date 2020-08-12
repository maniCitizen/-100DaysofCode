def removechar(str,n):
    first_part = str[:n-1]
    last_part = str[n:]
    print(first_part+last_part)
    
removechar("Python",6)
