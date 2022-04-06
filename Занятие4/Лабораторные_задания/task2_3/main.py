def task(num):  # TODO добавить аннотацию типов
    list_dig = [abs(int(dig)) for dig in str(abs(num))]
    sum_ = sum(list_dig)
    if 100 > sum_ // 10 > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
