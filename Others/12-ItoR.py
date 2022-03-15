def I (num):
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    res = ""
    L = ["I","V","X","L","C","D","M"]
    M = num // 1000
    num = num % 1000
    C = num // 100
    num = num % 100
    X = num // 10
    num = num % 10
    I = num
    # print("I=",I)
    # print("X=",X)
    # print("C=",C)
    # print("M=",M)

    j=0
    for item in (I,X,C,M):
        if item < 4:
            for i in range (item):
                res = L[j*2] + res
        elif item == 4:
            res = L[j*2] + L[j*2+1] +res
        elif item >= 5 and item !=9:
            for i in range (item-5):
                res = L[j*2] + res
            res = L[j*2+1] + res
        elif item == 9:
            res = L[j*2] + L[j*2+2] + res
        j+=1
    return res


def main():
    N = 49
    print(I(N))
    N = 147
    print(I(N))
    N = 1994
    print(I(N))
    N = 3999
    print(I(N))

main()