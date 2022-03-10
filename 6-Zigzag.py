def C (s,n):
    q = len(s) // (2 * (n - 1))
    # r = len(s) % (2 * (n - 1))
    # print("q=",q)
    # print("r=",r)
    res = ""
    for i in range(n):
        for j in range (q+1):
            if i == 0 and (j * 2 * (n - 1) < len(s)):
                res += s[j * 2 * (n - 1)]
                # print(j * 2 * (n - 1))
                # print(s[j * 2 * (n - 1)],end='')
            elif i == n - 1 and  (i + j * 2 * (n - 1) < len(s)):
                res += s[i + j * 2 * (n - 1)] 
                # print(s[i + j * 2 * (n - 1)] ,end=' ')
            elif i > 0 and i<n-1:
                if (i + j * 2 * (n - 1) < len(s)):
                    res += s[i + j * 2 * (n - 1)]
                    # print(s[i + j * 2 * (n - 1)],end='')
                if (2 * (n - 1) - i + j * 2 * (n - 1) < len(s)):
                    res += s[2 * (n - 1) - i + j * 2 * (n - 1)]
                    # print(s[2 * (n - 1) - i + j * 2 * (n - 1)],end='')
        print()
    return res


def main():
    # print(C("0123456789",5))
    print(C("ABCD",3))

main()
