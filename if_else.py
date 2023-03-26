# 1. if else statement
is_male = False

if is_male:
    print('You are a male')
else:
    print('You are a female')


# 2. More than one condition using (or) operator
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


# 3. More than one condition using (and) operator
is_male = True
is_tall = False

if not is_male and not is_tall:
    print("You are a tall male")
else:
    print("You are either male or tall or neither")


# 4. elif statement and not operator
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a male but not tall")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")
