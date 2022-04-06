def digit_sum(num: int) -> bool:
    list_ = [int(dig) for dig in str(num)]
    if 100 > num // 1000 > 0 and sum(list_) % 7 == 0:
        return True
    else:
        return False


    ...  # TODO проверить кратность суммы цифр


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))
