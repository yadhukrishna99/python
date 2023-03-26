try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide a number by 0")
except ValueError as err:
    print(err)

