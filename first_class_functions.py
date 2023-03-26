# A first class function or higher order function are the one that takes a function as a parameter or returns a function
# We can assign a function to variable, we can pass a function as a argument and also we can return a function
# This process that takes place in the code are called closures

# First lets see a first class function that takes a function as a argument

def cube(x):
    return x * x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


answer = my_map(cube, [1, 2, 3, 4, 5])
print(answer)


# Now we can see a first class function returning a function

def msg(log):

    def with_log():
        print("LOG:", log)
    return with_log

msg_1 = msg("Success")
msg_1()

# Another example for a function returning a function

def html_tag(tag):

    def with_statement(msg):
        print('<{0}> {1} </{0}>'.format(tag, msg))
    return with_statement


tag_h1 = html_tag("h1")
tag_h1("footer!")
tag_h1("header!")
