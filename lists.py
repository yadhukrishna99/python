# part 1 of lists
friends = ["Akilesh", "Arpu", "Prem", "Venkatesh", "Zubair"]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:4])
print(friends[-4:-2])
print(friends[-2:-4])
print(friends[0:4:2])
print(friends[ : :-1])

# replace a element in a list using index value
friends[1] = "Perterson"
print(friends[1])

# List functions
lucky_numbers = [9, 99, 999, 9999]
friends = ["Akilesh", "Arpu", "Prem", "Venkatesh", "Zubair"]

# 1. add an element at the end of a list
friends.append("Anurag")
print(friends)

# 2. add an element at any position in the list
friends.insert(4, "Salman")
print(friends)

# 3. combining two lists
friends.extend(lucky_numbers)
print(friends)

# 4. to remove elements in a list
friends.remove(9999)
print(friends)

# 5. to clear all the elements in the list
friends.clear()
print(friends)

# 6. pops or removes the last element of the list
number = lucky_numbers.pop()
print(number)
print(lucky_numbers)

# 7. to find the index of a element
friends = ["Akilesh", "Prem", "Venkatesh", "Zubair", "Arpu"]
print(lucky_numbers.index(99))
print(friends.index("Venkatesh"))

# 8. to count the repetition of a element in a list
print(friends.count("Arpu"))
print(lucky_numbers.count(9))

# 9. to sort a list
# friends.sort()
sorted_friends = sorted(friends)
print(sorted_friends)
print(friends)
friends.sort(reverse=True)
print(friends)


# 10. to reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

# 11. to copy a list to another variable
friends2 = friends.copy()
print(friends2)

nums = [1, 9, 3, 8, 6]
print(min(nums))
print(max(nums))
print(sum(nums))


for i in nums:
    print(i)

# using enumerate function to get the indexes along with values
for index, num in enumerate(nums, start=1):
    print(index, num)

# join and split functions
# to convert a list to a string use join()
subjects = ['Maths', 'Physics', 'Chemistry', 'Computerscience']
sub_str = ' - '.join(subjects)
print(sub_str)

# to convert a string to a list use split()
sub_lst = sub_str.split(' - ')
print(sub_lst)

list = [1, 5, 6, 0, 0, 0, 2, 67]
print(min(list))

