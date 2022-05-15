def U(m,n):
    D = m + n - 2
    C = n - 1
    res = 1
    c = 1
    for i in range(C, 0, -1):
        res *= D
        c *= i
        D -= 1
    # print("c = ",c)
    res //= c
    
    return res



def main():
    M=3
    N=2
    print(U(M,N))
    M=7
    N=3
    print(U(M,N))
    M=6
    N=1
    print(U(M,N))


main()