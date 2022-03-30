# TODO написать функцию для поиска необходимой суммы денег
def zanachka(salary, spend, month, koef):
    tot_sal = salary * month
    tot_spen = 0
    for n in range(month):
        tot_spen = tot_spen + spend
        spend = spend * koef

    nichka = tot_spen - tot_sal

    return nichka




if __name__ == "__main__":
    print(zanachka(50000, 55000, 10, 1.03))
