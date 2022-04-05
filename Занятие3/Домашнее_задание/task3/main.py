def get_max_length_word(str_words):
    str_ = str_words.split(' ')  # TODO получить список непустых слов

    max_len = 0  # пусть изначально длина самого длинного слова равна 0
    for word in str_:  # TODO пройти по всем словам и найти самую большую длину
        if len(word) > max_len:
            max_len = len(word)
    ...  # TODO составить список из слов, длина которых равна самой большой
    list_ = []
    for word in str_:
        if len(word) == max_len:
            list_.append(word)
    return list_

if __name__ == "__main__":
    print(get_max_length_word("раз два три"))
    print(get_max_length_word("раз два три четыре"))
