def R(x):
    if x == 0: return 0
    N = 0
    if x < 0: 
        N = 1 
        x = -x

    flag = 1
    res = 0
    while flag == 1:
        temp = x % 10
        res = res * 10 + temp
        x = x // 10
        if x == 0: flag =0
    if res < 2 ** -31 or res> 2 ** 31 - 1 : return 0
    if N == 1: res = -res
    return res



def main():
    y=100
    print(y)
    print(R(y))
    y=123
    print(y)
    print(R(y))
    y=-52
    print(y)
    print(R(y))
    y=0
    print(y)
    print(R(y))

main()