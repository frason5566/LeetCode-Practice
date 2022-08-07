def C(n):
    a = 1
    e = 1
    i = 1
    o = 1
    u = 1
    for _ in range(1,n):
        a, e, i, o, u = e+i+u, a + i, e + o, i, i + o
    return (a+e+i+o+u) % 1000000007



def main():
    print(C(1))
    print(C(2))
    print(C(3))
    print(C(4))
    print(C(5))

main()
