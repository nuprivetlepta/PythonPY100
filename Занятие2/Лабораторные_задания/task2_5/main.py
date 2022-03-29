list_ = [1, 0, 2, 1]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

# TODO посчитать количество четных и нечетных значений в списке
for num in list_:
    if num % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

if count_even > count_odd:
    print('Четных чисел больше')
elif count_even == count_odd:
    print('Всех поровну')
else:
    print('Нечетных чисел больше')
