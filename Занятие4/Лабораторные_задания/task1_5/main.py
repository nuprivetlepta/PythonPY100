if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_odd = [num for num in list_ if num % 2 != 0]
    list_even = [numi for numi in list_ if numi % 2 == 0]

    len_odd = len(list_odd)
    len_even = len(list_even)

    if len_odd > len_even:
        print(list_odd)
    elif len_even > len_odd:
        print(list_even)
    else:
        print('количества элементов равны')
