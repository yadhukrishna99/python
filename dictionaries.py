monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv", "Love"))

monthConversions['Luv'] = 'I love you'
print(monthConversions.get('Luv'))

# to update a dictionary
student = {'name': 'Yadhu', 'age': 23, 'sub': ['Math', 'Compsci']}
print(student)

student.update({'name': 'Akil', 'age': 22})
print(student)

# to delete a key inside dictionary
del student['age']
print(student)

subjects = student.pop('sub')
print(student)
print(subjects)

print(len(monthConversions))
print(monthConversions.keys())
print(monthConversions.values())
print(monthConversions.items())

# looping through dictionary
for key, value in monthConversions.items():
    print(key, value)

