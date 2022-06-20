def H(n):
    def h(n,his):
        cnt = 0
        while n != 0:
            d = n % 10
            cnt +=d ** 2
            n //= 10
        if cnt != 1 and cnt not in his:
            his.append(cnt)
            return h(cnt,his)
        elif cnt in his:
            return False
        elif cnt == 1:
            return True
    return h(n,[])

def main():

    print(H(19))
    print(H(2))

main()