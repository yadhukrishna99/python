# list comprehensions are used to create a list in a easier and more readable way

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# EX.1. I want 'n' for each 'n' in nums

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

my_list = [n for n in nums]
print(my_list)


# EX.2. I want 'n*n' for each 'n' in nums

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

my_list = [n*n for n in nums]
print(my_list)


# EX.3. I want 'n' for each 'n' in nums if 'n' is even

# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)


# EX.4. I want (letter, num) pair for each letter in 'abcd' and for each num in '0123'

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
