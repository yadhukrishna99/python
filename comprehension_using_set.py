nums = [1, 1, 2, 3, 4, 5, 4, 3, 6, 6, 7, 8, 9, 8, 7, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)