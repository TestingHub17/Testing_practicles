# The map() function takes a function and applies it to each element in an iterable and generating the new iterable
# containing transformed  list

# Provide an example where you use map() to increase all numbers in a list by one.

data = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x:x+1 , data))
print(result)


def increase(x):
    return x+1

result = list(map(increase, data))
print(result)