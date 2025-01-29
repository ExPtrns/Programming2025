def _check_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def check_date(date):
    if len(date) != 10:
        return False
    date_list = list(map(int, date.split(".")))
    if not 1 <= date_list[1] <= 12 or not 1 <= date_list[2] <= 9999:
        return False
    day_month = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if _check_year(date_list[2]):
        day_month[2] = 29
    else:
        day_month[2] = 28
    if date_list[0] in range(1, day_month[date_list[1]]+1):
        print(f'{date_list[0]}.{date_list[1]}.{date_list[2]}')
        return True
    else:
        print(f'{date_list[0]}.{date_list[1]}.{date_list[2]}')
        return False



if __name__ == '__main__':
    print(check_date('31.11.2045'))
