if __name__ == "__main__":
    # Write your solution here
    list_ = [1, 2, 3, 4, 5, 88, 7, 8, 9, 99]    # Nash spisok
    max_value = 0    # Nashe maximalnoe znachenie
    i_max = 0   # Index maximuma
    for index, value in enumerate(list_):
        if value > max_value:     #perebiraem nash spisok, ischem maximum
            max_value = value         # perezapisivaem maximum po usloliju
            i_max = index       # perezapisivaem index
    list_[i_max] = list_[0]     # prisvaivaem maximalnomu uchastniku velichinu pervogo componenta
    list_[0] = max              # prisvaivaem pervomu componentu znachenie max

    print(list_)
    print(max, i_max)







