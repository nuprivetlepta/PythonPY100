def task(num: int):
    def_list = [int(dig) for dig in str(num)]  # TODO сформировать список цифр

    if 9 in def_list or 4 in def_list and 8 in def_list:  # TODO записать условие
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
