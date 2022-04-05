# TODO написать функцию для поиска количества месяцев
def alive(money_capital, salary, spend, koef):
    trat_ = spend
    total_bank = money_capital + salary
    month = 0
    total_spend = spend
    while True:
        print(total_bank, total_spend)
        if total_bank >= total_spend:
            total_bank = total_bank + salary
            trat_ = trat_ * koef
            total_spend = total_spend + trat_
            month = month + 1

        else:
            return month





if __name__ == "__main__":
   print(alive(6000, 15000, 20000, 1.05))
