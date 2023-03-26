# Static methods does not take either instance or a class as a parameter
# It behaves like normal function, this can be used inside the class where we dont want to work with any instance variables or class variables


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

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Yadhu", "Krishna", 40000)
emp_2 = Employee("Nithish", "Kumar", 60000)

import datetime

my_date = datetime.date(2023, 1, 10)
print(Employee.is_working(my_date))


