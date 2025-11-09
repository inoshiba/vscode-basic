from datetime import datetime

date_str = "2024-05-01"
requested_day = datetime.strptime(date_str, '%Y-%m-%d').date()
today_date = datetime.today().date()
diff_day = today_date - requested_day
print(diff_day.days)

import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1),quantity)

    numbers.sort()
    
    return numbers
print(get_numbers_ticket(1, 49, 6 ))