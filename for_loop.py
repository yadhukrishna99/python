# looping through a string
for letter in "Girafee Academy":
    print(letter)

# loop through a list
friends = ["Akilesh", "Arpu", "Zubair", "Prem"]
for friend in friends:
    print(friend)

# looping through range
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(len(friends)):
    print(friends[i])


# using break statement
friend = ["Akilesh", "Arpu", "Zubair", "Prem", "Venkatesh"]
for i in friend:
    if i == "Zubair":
        print("Found!!")
        break
    print(i)


# using continue statement
friend = ["Akilesh", "Arpu", "Zubair", "Prem", "Venkatesh"]
for i in friend:
    if i == "Zubair":
        print("Found!!")
        continue
    print(i)
