DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Введите год рождения:"))  # TODO запросить у пользователя год рождения
current_year = int(input("Введите текущий год:"))  # TODO запросить у пользователя текущий год
days_alive = (current_year - start_year) * 365
print(days_alive)  # TODO посчитать и распечатать количество прожитых дней
