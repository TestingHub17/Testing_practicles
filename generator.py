# A generator function is a special type of function that returns an iterator object.
# Instead of using return to send back a single value, generator functions use yield to produce a series of results over time.


# def prime(min, max):
#
#     yield number
#
#
# min = eval(input("Enter min range"))
# max = eval(input("Enter max range"))
# for data in prime(min, max):
#     print(data)








def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

for n in fun(5):
    print(n)