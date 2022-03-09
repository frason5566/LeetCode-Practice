def O(s):
    flag = 1
    res = []
    for i in range (1,len(s)):
        while flag==1:
            if s[i] == s[i-1]:
                


def main():
    S1="babad"
    S2="baad"
    print(O(S1))
    print(O(S2))


main()