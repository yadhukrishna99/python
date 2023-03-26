# Instance variables are unique for each instances of the class.
# But class variables are same for all instances of the class.

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def pay_increment(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee("Yadhu", "Krishna", 40000)
emp_2 = Employee("Nithish", "Kumar", 60000)
emp_3 = Employee("Prem", "Kumar", 100000)

print(emp_1.pay)
emp_1.raise_amount = 1.1
emp_1.pay_increment()
print(emp_1.pay)
print(emp_2.pay)

# Employee.raise_amount = 1.1
# emp_1.raise_amount = 1.1
# emp_2.raise_amount = 1.1


print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)
