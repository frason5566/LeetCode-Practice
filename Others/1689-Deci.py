def D(n): # Time limit
    n = int(n)
    res = 0
    while n > 0:
        temp = n % 10
        res = max(res, temp)
        n //=10
    return res

def DD(n):
    return max(n)


def main():
    print(D("32821"))

main()
