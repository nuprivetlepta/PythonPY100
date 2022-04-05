def is_palindrome(str_: str):
    our_s = (str_.lower()).split()
    our_s = "".join(our_s)
    if our_s == our_s[::-1]:
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
    is_palindrome("ты вредитель")
    is_palindrome("God saw I was Dog")
