def main():
    n = 1  # первое натуральное число
    current_sum = 0  # текущая сумма
    max_sum = 500  # максимальная сумма
    while True:
        if current_sum + n ** 2 > max_sum:
            break

        current_sum = current_sum + n ** 2
        n = n + 1

    return n, current_sum
if __name__ == "__main__":
    count_numbers, sum_ = main()
    print(count_numbers, sum_)
`