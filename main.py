import random


def get_numbers_ticket(min, max, quantity):
    num = random.sample(range(min, max), quantity)
    if min < 1 or max > 1000:
        return 'Your number is out of range'
    else:
        return num


print(f'Your tiket numbers: {get_numbers_ticket(1, 1000, 6)}')
