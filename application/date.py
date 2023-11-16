import datetime


def today_date():
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%d.%m.%Y')
    print(formatted_date)


if __name__ == '__main__':
    today_date()
