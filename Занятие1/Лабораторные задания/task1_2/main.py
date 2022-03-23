pay = int(input("Введите вашу заработную плату: "))  # Напишите ваше решение
taxes = pay * 0.13
salary = pay - taxes
print("Удержанный налог:", taxes,  "Сумма на руки:", salary)