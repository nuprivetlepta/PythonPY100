def get_year_count(start_money, inflation):
    current_money = start_money  # TODO установить текущую сумму, которая будет с каждым годом уменьшаться
    count_years = 0
    while current_money > start_money / 2:
        current_money = current_money * (1 - inflation)
        count_years += 1

    # TODO найти минимальное количество лет

    return count_years


if __name__ == "__main__":
    print(get_year_count(10000, 0.2))
