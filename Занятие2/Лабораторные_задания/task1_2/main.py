if __name__ == '__main__':
    A, B = int(input()), int(input())
    cond_1 = A % 2 == 1
    cond_2 = B % 2 == 1
    if cond_1 and cond_2:
        print('Они и вправду нечётные')
    else:
        print('Кто-то чётный')