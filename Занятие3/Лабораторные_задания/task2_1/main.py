def task(str1: str, str2: str, k: int):
    sl1 = str1[:k]
    sl2 = str2[:k]
    if sl1 == sl2:
        print('ДА')
    else:
        print('НЕТ')




if __name__ == "__main__":
    task("abc", "abcde", 3)
    task("abcba", "abcde", 5)
