if __name__ == '__main__':
    A, B = int(input("Введите первое число: ")), int(input("Введите второе число: "))
    sum_of_sq = A**2 + B**2
    sq_of_sum = (A + B)**2
    cond_1 = sum_of_sq > sq_of_sum
    cond_2 = sum_of_sq < sq_of_sum
    if cond_1:
        print("Cумма квадратов больше, чем квадрат суммы")
    elif cond_2:
        print("Квадрат суммы больше, чем сумма квадратов")