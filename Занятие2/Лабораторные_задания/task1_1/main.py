if __name__ == "__main__":   # TODO
    a = int(input("введите число:"))
    condition_1 = a % 2 == 0
    condition_2 = a % 3 == 0
    if condition_1 == True or condition_2 == True:
        print('Подходит')
    else:
        print("Не то пальто")
