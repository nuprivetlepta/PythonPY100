if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]

    new_list = [digit - (sum(list_) / len(list_)) for digit in list_]  # TODO Заполните список с помощью list comprehension

    print(new_list)
