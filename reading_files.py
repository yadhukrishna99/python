# syntax to open a file -- open("file_name", "mode")
# modes----
# "r" -- readonly
# "w" -- writeonly, (ie) it will overwrites an existing file or creates a new file
# "a" -- append
# "r+" -- read and write
# syntax to close a file -- file_name.close()


# to check whether the file is readable
employee_file = open("employee.txt", "r")
print(employee_file.readable())
employee_file.close()


# to read the entire file
employee_file = open("employee.txt", "r")
print(employee_file.read())
employee_file.close()


# to read a single line in a file
employee_file = open("employee.txt", "r")
print(employee_file.readline())
employee_file.close()


# to read every line in the file in the form of list
employee_file = open("employee.txt", "r")
print(employee_file.readlines())
employee_file.close()


# to read a particular line in a file by using index value
employee_file = open("employee.txt", "r")
print(employee_file.readlines()[1])
employee_file.close()


# using for loop with readlines() to print each line
employee_file = open("employee.txt", "r")
for i in employee_file.readlines():
    print(i)
employee_file.close()
