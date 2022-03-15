def H(n):
    cnt = 0
    while n > 0:
        cnt += n % 10
        n = n // 10
    return cnt

def main():
    n = 1
    print(H(n))
    n = 1011
    print(H(n))
    n = 11111111111111111111111111111101
    print(H(n))

main()