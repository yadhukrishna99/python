class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee("Yadhu", "Krishna", 40000)
emp_2 = Employee("Nithish", "Kumar", 60000)

print(emp_1.pay)
print(emp_2.pay)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_2))

