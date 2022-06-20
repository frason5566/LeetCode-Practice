def P(digits):
    d = len(digits) - 1
    digits[d] += 1
    while d > 0:
        if digits[d] == 10:
            digits[d] = 0
            digits[d-1] += 1
            d -= 1
        else:
            break
    if digits[0] == 10:
        digits = [1,0] + digits[1:] 

    return digits


def main():
    D = [1,2,3]
    print(P(D))
    D = [9,9,9]
    print(P(D))

main()