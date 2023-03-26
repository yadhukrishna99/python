print("Hello World!!")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")


# VARIABLES
character_name = "John"
character_age = "50"
print("There lived a man named " + character_name + ",")
print("He was " + character_age + "years old.")
print("He really liked his name " + character_name + ",")
print("But he did not like being " + character_age + ".")

# Note, for string concatenation we can use f strings
msg_1 = 'hello'
msg_2 = 'world'
message = f'{msg_1.upper()} {msg_2}'
print(message)

# Working with strings
phrase = "Giraffe Academy"
print(phrase)
print("Giraffe\nAcademy")
print("Girafee'Academy")
print("Girafee\"Academy")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.lower().islower())
print(phrase[0])
print(phrase[14])
print(phrase.index("f"))
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Tiger"))



# Working with numbers
print(5)
print(5 + 5)
print(10 + 9.9)
print(5 * 2 + 5)
print(5 * (2 + 5))
my_num = 9
print(str(my_num) + " is my fav number")
print(abs(-9))
print(pow(2, 3))
print(max(2, 5))
print(min(2, 5))
print(round(3.5))
print(round(3.3))
from math import *
print(floor(3.7))
print(ceil(3.3))
print(sqrt(49))


# Getting input from user
name = input("What is your name ? ")
age = input("What is your age ? ")
print("Hii " + name + " ! you are " + age)
# (or)
print(f'Hii {name} ! you are {age}')


# if we want to see the list of functions we can use for our object then use
a = 5
b = 'yadhu'
print(dir(a))
print(dir(b))

# if we want to see what a specific function does or list of functions with usages then use
print(help(str))
print(help(len))



