
def input_numbers():
    list_numbers = []
    input_num = 0
    while input_num >= 0:
        input_num = int(input("Введите новое число:"))

        if 3 <= input_num <= 13:
            list_numbers.append(input_num)

    list_numbers.append(input_num)

    return list_numbers


if __name__ == "__main__":
    print(input_numbers())