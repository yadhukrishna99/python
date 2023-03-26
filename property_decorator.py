# By using property decorators we can access our method like an object
# Thus, gives our method getter, setter and deleter properties



class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = self.first_name + '.' + self.last_name + '@gmail.com'

    @property
    def email(self):
        return '{} {}@gmail.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print("Deleted employee name")
        self.first_name = None
        self.last_name = None


emp_1 = Employee("Yadhu", "Krishna", 40000)
print(emp_1.first_name)
emp_1.first_name = "Corey"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)


emp_1.fullname = 'Corey Shafer'

print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.email)

del emp_1.fullname
print(emp_1.first_name)

