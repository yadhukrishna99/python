def hello_func():
    pass


print(hello_func())


def greet(greeting, name='you'):
    return "{}, {}".format(greeting, name)


print(greet('HI').lower())
print(greet('Hii', 'Yadhu').upper())


# using *args and **kwagrs
# it allows a function to take any number of positional and keyword arguments
def stud_info(*args, **kwargs):
    print(args)
    print(kwargs)


stud_info('Math', 'CompSci', name='Yadhu', age=23)


# unpacking the arguments from a list or dictionary
def stud_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Maths', 'Physics', 'Chemistry', 'CompSci']
data = {'name': 'Yadhu', 'age': 23}

stud_info(*courses, **data)

