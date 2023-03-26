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

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Here __init__,__repr__ and __str__ are special methods
    # When we print a object name the __repr__ method will be called, but if __str__ method is given then, __repr__ will not be called
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "'{}', '{}'".format(self.fullname(), self.email)

    # Here __add__ is also a special method, it is called when we use the + operator.
    # We have modified the + operators function to add the pay of the employees
    def __add__(self, other):
        return self.pay + other.pay

    # __len__ is a special method which is used to get the lenth of a string,here we modified its function
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Yadhu", "Krishna", 40000)
emp_2 = Employee("Nithish", "Kumar", 60000)

print(emp_1)
print(emp_2)

print(1 + 1)
print(emp_1 + emp_2)

print(len(emp_1))
print(len(emp_2))

