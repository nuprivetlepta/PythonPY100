def task(src_list: list) -> list:  # TODO записать решение в виде функции
   return [num ** 3 if num >= 0 else num - num for num in src_list]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    new_list = task(list_)
    print(new_list)