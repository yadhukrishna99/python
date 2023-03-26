month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        print("Invalid Month")
        return
    if month == 2 and leap_year(year):
        print("29")
    else:
        print(month_days[month])


while True:
    x = input("\n\nIf u want to check leap year, then press 1\nIf u want to find no of days, then press 2: ")
    if x == '1':
        y = int(input("Enter a year: "))
        print(leap_year(y))
    elif x == '2':
        year = int(input("Enter a year: "))
        month = int(input("Enter the month in number: "))
        days_in_month(year, month)
    else:
        print("Invalid type")
