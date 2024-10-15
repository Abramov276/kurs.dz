# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, '%Y.%m.%d').date()


# def date_today():
#     return datetime.today().date()


# def date_difference(date_birth):
#     birthday = string_to_date(date_birth)

#     return (date_today() - birthday).days


# print(string_to_date("2000.8.12"))
# print(date_today())
# print(date_difference("2024.12.12"))

from datetime import datetime, timedelta


# def get_days_from_today(date):

#     given_date = datetime.strptime(date, '%Y.%m.%d').date()
#     today = datetime.today().date()
#     difference = (today - given_date).days

#     return difference


# print(get_days_from_today("2024.06.12"))

import random


def get_numbers_ticket(min, max, quantity):
    num = random.sample(range(min, max), quantity)
    if min < 1 or max > 1000:
        return 'Your number is out of range'
    else:
        return num


print(f'Your tiket numbers: {get_numbers_ticket(1, 1000, 6)}')
