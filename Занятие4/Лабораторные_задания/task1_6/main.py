if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    our_compare = list_[0]
    list_great_first = len([num for i, num in enumerate(list_) if num > list_[0]])  # TODO отфильтровать элементы больше первого

    print(list_great_first)
