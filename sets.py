# sets are unordered, ie each time we print a set the order of the elements changes
# sets does not takes duplicates
cs_courses = {'Maths', 'Physics', 'Computer', 'Chemistry', 'Chemistry'}
art_courses = {'Maths', 'Physics', 'Accounts', 'Stat'}

print(cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Important to note, while creating empty list, tuple and sets

# to create an empty list
# empty_lst = []
# emty_lst = list()

# to create an empty tuple
# empty_tuple = ()
# emty_tuple = tuple()

# to create an empty set
# empty_set = {} - this is wrong, this creates an empty dict
# emty_set = set()
