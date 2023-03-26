names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

# I want a dict {'hero': 'name'} for each name, hero in list(zip(names, heroes))
# my_dict = {}
# for name, hero in list(zip(names, heroes)):
#     my_dict[name] = hero
# print(my_dict)

my_dict = {name: hero for name, hero in list(zip(names, heroes))}
print(my_dict)

# If i dont want a particular name of the hero then
my_dict1 = {name: hero for name, hero in list(zip(names, heroes)) if name != 'Peter'}
print(my_dict1)