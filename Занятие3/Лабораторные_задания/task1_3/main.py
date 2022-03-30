def get_list_number_divisors(number):
    list_ = []
    for m in range(1, number+1):
        if number % m == 0:
            list_.append(m)


    return list_



if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
    print(2**16)