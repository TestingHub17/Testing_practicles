# decorator is used to enhance the functionality of existing function or method, like it extends the behaviour of actual code





def decorator(func):

    def check_number(a, b):
        if b == 0:
            return "Divide by zero not allowed"
        else:
            return func(a,b)

    return check_number


def divide(a,b):
    return a/b


print(decorator(divide)(2,3))







#
#
#
#
# from  time import sleep, time
#
# def my_decorator_func(func):
#     def wrapper_func():
#         # Do something before the function.
#         start_time = time()
#         func()
#         end_time = time()
#         time_difference = (end_time - start_time)
#         print(f"Execution time of program is:  {time_difference:.6f}")
#         # Do something after the function.
#     return wrapper_func
#
# def ordinary():
#     sleep(15.36)
#     print("I am ordinary")
#
# d = my_decorator_func(ordinary)
# print(d())


