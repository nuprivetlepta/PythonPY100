if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5      # TODO чему равно начальное смещение?
    for index, value in enumerate(phrase):# TODO как использовать начальное смещение в команде enumerate?
        index = (index+5) * " "
        print(index, value)