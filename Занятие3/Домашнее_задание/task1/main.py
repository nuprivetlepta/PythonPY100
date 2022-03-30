def input_numbers():
    list_numbers = []

    while True:
        input_num = int(input("Введите новое число:"))
        if input_num < 0:
            break

        if 3 <= input_num >= 13:
            list_numbers.append(input_num)

    return list_numbers


if __name__ == "__main__":
    input_numbers()
    print(input_numbers)
