def get_unique_words(str_words: str):
   list_words = str_words.lower().split()
   join_them = ", ".join(list_words)
   my_set = {join_them}
   return set(list_words)


if __name__ == "__main__":
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))