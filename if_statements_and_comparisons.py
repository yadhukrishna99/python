def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
print(max_num(6, 49, 37))
print(max_num(99, 99, 32))


# List of comparison operators
# <   -  less than
# >   -  greater than
# <=  -  less than and equals
# >=  -  greater than and equals
# ==  -  equals
# !=  -  not equals

# false values
# False
# None
# any zero numeric type
# '', (), {}, []

condition = 0
if condition:
    print('True')
else:
    print('False')


# Note
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
a = b
print(a is b)
