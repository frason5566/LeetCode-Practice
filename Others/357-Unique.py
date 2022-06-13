def U(n):
    if n == 0: return 1
    def h(i):
        if i == 1:
            return 10
        res = 9*9
        for j in range(1,i-1):
            res *= 9-j
        return res + h(i-1)


    return h(n)

def main():
    print(U(0))
    print(U(1))
    print(U(2))
    print(U(3))
    print(U(4))
    print(U(5))
    print(U(6))
    print(U(7))
    print(U(8))

main()