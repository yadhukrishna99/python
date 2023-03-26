# Instance methods takes the instance of the class as the first parameter(ie, self) as seen in previous examples
# Class methods works with the class variables and takes class as the first parameter

class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + "@gmail.com"

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)


emp_1 = Employee("Yadhu", "Krishna", 40000)
emp_2 = Employee("Nithish", "Kumar", 60000)
print(Employee.raise_amount)
print(emp_1.raise_amount)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)

# class methods is also called as alternative constructors. ie, we can create objects for the class
emp_str_1 = "John-Adams-20000"
emp_str_2 = "Kelly-Richard-50000"
emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
print(emp_3.pay)
print(emp_4.pay)
print(emp_3.email)