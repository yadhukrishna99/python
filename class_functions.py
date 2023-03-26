# class functions are used to give extra information or modify the strucures of the class object
# class functions are accessed by the objects of the class

class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 9.5:
            return True
        else:
            return False


student1 = Student("Yadhu", "Civil", 8.9)
student2 = Student("Kalyani", "MSC", 9.5)
print(student1.on_honor_roll())
print(student2.on_honor_roll())
