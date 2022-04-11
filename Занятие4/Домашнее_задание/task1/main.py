def task(num: int) -> bool:
    # TODO какая есть особенность, когда все цифры в числе одинаковые?
    chislo = str(num)
    for i in range(len(chislo)):
        if chislo[i] != chislo[0]:
            return False
    return True


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
