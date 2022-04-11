def task(num: int) -> bool:
    str_ = str(int)
    ...  # TODO какая есть отличительная особенность, при повторяющихся числах
    list_ = [digit for digit in str(num)]
    set_ = set(list_)
    return True if len(list_) != len(set_) else False


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))