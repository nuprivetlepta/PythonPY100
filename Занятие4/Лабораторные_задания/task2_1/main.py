if __name__ == "__main__":
    number = 123456789

    list_digits = [int(dig) for dig in str(number)]  # TODO c помощью list comprehension получить список цифр числа
    print(list_digits)

    print(sum(list_digits))  # TODO найти сумму цифр числа

    print(sum([dig for dig in list_digits if dig % 2 == 0]))  # TODO найти сумму всех четных чисел

    print(len(list_digits))  # TODO найти количество цифр

    print(min(list_digits))  # TODO найти минимальную цифру

    print([dig for i, dig in enumerate(list_digits) if i % 2 == 0])  # TODO все цифры стоящие на нечетных местах

    print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
