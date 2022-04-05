def check_string(str_):
    if len(str_) != 0:
        for sym in str_:
            if sym != "0" and sym != "1":
                return False
        return True
    else:
        return False
    # if len(str_) != 0:
    #     for i in range(len(str_)):
    #         if str_[i] != '1' and str_[i] != '0':
    #             return False
    #     return True
    # else:
    #     return False






if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
