class Student:

    def __init__(self, m1, m2, m3, m4, m5):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = self.m3 + other.m3
        s4 = self.m4 + other.m4
        s5 = self.m5 + other.m5
        total = s1 + s2 + s3 + s4 + s5
        return total

    def __gt__(self, other):
        s1 = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        s2 = other.m1 + other.m2 + other.m3 + other.m4 + other.m5
        if s1 > s2:
            return"Yes"
        return"No"

    def total(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        return total

    def avg(self):
        avg = (self.m1 + self.m2 + self.m3 + self.m4 + self.m5) / 5
        return avg


s1 = Student(80, 76, 90, 72, 97)
s2 = Student(74, 88, 92, 90, 68)

print(s1 + s2)
print(s2 > s1)
print(s1.avg())
print(s2.avg())
print(s1.total())
print(s2.total())
