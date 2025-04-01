# In Python, implement a generator function that yields prime numbers in a specified range.

def is_prime_number(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
        return True


def generate_prime(min, max):
    for num in range(min, max):
        if is_prime_number(num):
            yield num


min, max = eval(input("enter two min, max number"))
for data in generate_prime(min, max):
    print(data)





















# Write a Python function using recursion to find a file with a specific extension within
# a nested folder structure. Report the path when found.

"""import glob
import os

extension = input("Enter the extension")


def find_file(path):
    files = glob.glob(f"{path}/*")
    for path in files:
        if os.path.isfile(path) and path.endswith(extension) and path.:
            return path
        if os.path.isdir(path):
            expected_path = find_file(path)
            if expected_path is not None:
                return expected_path

current_directory = os.getcwd()
print(find_file(current_directory))"""












# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional
#         # Part as Answer
#         result = x // y
#         print(result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     finally:
#         print("Yeah ! Your answer is :")
#
#     # Look at parameters and note the working of Program
#
#
# # divide(3, 2)
#
# divide(3, 0)
#
# dd = {(0,0,1,2,3):"hello", (1,2,3):"World", 4.5:"45", 56:54}
# print(dd)
#
# tup = (0,0,1,2,3)
# ll = list(tup*0)
# print(ll)
# print(tup[0])
# a,b,*c = tup
# print(a)