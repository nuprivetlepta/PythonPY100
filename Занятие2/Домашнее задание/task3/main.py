# TODO
A = int(input())
B = int(input())
C = int(input())
list_ = [A, B, C]
count = 0   # Переменная для подсчёта удовлетворяющих условию переменных
for digit in list_:
    if digit < 45:
        count = count + 1
print ('количество чисел меньших 45:', count)
print(count==1)