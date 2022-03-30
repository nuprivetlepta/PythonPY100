
def factorial(n):
    o = 1
    for m in range(1, n + 1):
        o = o * m
    return o

if __name__ == "__main__":
    n = 5
    print(factorial(n))
