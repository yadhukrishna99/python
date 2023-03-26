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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.50

    def __init__(self, first_name, last_name, pay, employee=None):
        super().__init__(first_name, last_name, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def rem_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print("-->", emp.fullname())


emp_1 = Employee("Yadhu", "Krishna", 30000)
dvp_1 = Developer("Nithish", "Kumar", 40000, 'Java')
mgr_1 = Manager("James", "Mithchel", 50000, [emp_1, dvp_1])


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(dvp_1.pay)
dvp_1.apply_raise()
print(dvp_1.pay)
print(dvp_1.fullname())
print(mgr_1.fullname())


mgr_1.print_emp()
print(mgr_1.pay)
mgr_1.apply_raise()
print(mgr_1.pay)

print(Employee.num_of_emps)

# This gives the details of the subclass
# print(help(Developer))
# print(help(Manager))

# This is to check whether an instance belongs to that class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# This is to check whether a class is subclass of that class
print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))
