# appending to an existing file
employee_file = open("employee.txt", "a")
employee_file.write("\nKelly --- Customer Service\nJimmy --- HR")
employee_file.close()

# overwriting an existing file or if a new file name is given then it will add the contents in that new file
employee_file = open("employee1.txt", "w")
employee_file.write("Human Resources")
employee_file.close()

