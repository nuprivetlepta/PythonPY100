def count_even_numbers(list_numbers: list) -> int:
    return len([num for num in list_numbers if num % 2 == 0])  # TODO найти количество четных чисел в списке list_numbers


if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
