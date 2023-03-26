# Decorators are functions that takes a function as an argument and adds functionality to that function without altering
# the source code of the original function

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function is executed before {} function".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("Display function is executed")

# we can also use same decorators for many number of functions
@decorator_function
def display_info(name, age):
    print("display_info executed this with arguments ({}, {})".format(name, age))

# display = decorator_function(display), this is equal to the @decorator_function
display()

display_info('Yadhu', 23)


# For practical example, we are using a program execution timer function


import time


def my_time(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} function takes {} time to run'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_time
def display_inf(name, age):
    time.sleep(2)
    print("display_info executed this with arguments ({}, {})".format(name, age))


display_inf('Yadhu', 23)


# when we use multiple decorators for a singe function, the original function will not be passed to the decorators
# properly,so we can use @wraps decorator to the wrappers inside the decorator function to wrap the original function
# instead of wrapper function.
# from functools import wraps






