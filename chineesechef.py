# Inheritance can be used to inherit functions from one class to the other and these functions can be accessed from that
# class

from chef import Chef

class ChineeseChef(Chef):

    def make_specialdish(self):
        print("Chef makes Chineese noodles")

