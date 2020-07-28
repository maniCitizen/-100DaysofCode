from functools import reduce

nums = [3,2,5,4,7,8,3,6,4,8,6]

evens  = list(filter(lambda n:n%2==0,nums))

print(evens)

doubles = list(map(lambda n:n*2, evens))

print(doubles)

sum = reduce(lambda a,b:a+b, doubles)

print(sum)