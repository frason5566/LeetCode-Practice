def S(num):
    step = 0
    while num > 0:
        if num % 2 == 1:
            num -= 1
        else:
            num //= 2
        step += 1
    return step

def main():
    print(S(14))
    print(S(19))
    # print(S(14))
    print(S(8))
    print(S(123))
    print(S(3))


main()