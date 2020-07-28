def long_length(lst):
    word_len = [(len(n),n) for n in lst]
    word_len.sort()
    return word_len[-1][1]
    
print(long_length(["PHP", "Exercises", "Backend",]))