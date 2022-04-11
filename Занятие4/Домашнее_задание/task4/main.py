def is_lucky_number(num: int) -> bool:
    ...  # TODO проверить что число шестизначное
    str_ = str(num)
    if len(str_) != 6:
        raise ValueError('Число не шестизначное')
    full_list = [int(num) for num in str_]
    return True if sum(full_list[3:]) == sum(full_list[:3]) else False

    # if len(str_) == 6:
    #     first_half = [int(str_[i]) for i in range(3)]
    #     full_str = [int(num) for num in str_]
    #     if sum(first_half) == sum(full_str) / 2:
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    print(is_lucky_number(123321))
    print(is_lucky_number(111111))
    print(is_lucky_number(123456))
    print(is_lucky_number(456243))
