from datetime import datetime, timedelta


def get_days_from_today(date):

    given_date = datetime.strptime(date, '%Y.%m.%d').date()
    today = datetime.today().date()
    difference = (today - given_date).days

    return difference


print(get_days_from_today("2024.06.12"))
