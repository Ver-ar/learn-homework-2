from datetime import date, datetime, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
   
    dt_now = datetime.now()
    dt_now.strftime('%d.%m.%Y %H^%M')
    delta_yesterday = timedelta(days = 1)
    dt_yesterday = dt_now - delta_yesterday
    delta_months = timedelta(days = 30)
    dt_months = dt_now - delta_months
    delta_tommorow = timedelta(days = -1)
    dt_tommorow = dt_now - delta_tommorow


    print (f"Сегодня {dt_now.strftime('%d.%m.%Y %H:%M')}")
    print (f"Вчера было {dt_yesterday.strftime('%d.%m.%Y %H:%M')}")
    print (f"Месяц назад было {dt_months.strftime('%d.%m.%Y %H:%M')}")
    print (f"Завтра будет {dt_tommorow.strftime('%d.%m.%Y %H:%M')}")


def str_2_datetime(date_string):
    
    date_dt2 = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print (date_dt2)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))