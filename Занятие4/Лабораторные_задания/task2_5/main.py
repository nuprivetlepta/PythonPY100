def is_palindrome_number(num: int) -> bool:
    if num < 0:
        raise ValueError('число отрицательное')
    list_ = [int(dig) for dig in str(num)]

    a = list_[::1] == list_[::-1]

    return a

if __name__ == "__main__":
    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))
