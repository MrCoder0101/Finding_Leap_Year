def is_leap(target_year):
    if target_year % 4 == 0:
        if target_year % 100 == 0:
            if target_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(taget_year, target_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """enter a year and month then find leap year or not"""
    if is_leap(taget_year) and month == 2:
        return 29
    return month_days[target_month - 1]


year = int(input("enter a year:"))
month = int(input("enter a month:"))
days = days_in_month(year, month)
print(days)
