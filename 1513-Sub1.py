def C (s):
    cnt = 0
    for i in range (len(s)):
        check = "1" * i
        for j in range (len(s)):

            print(check)

    return cnt

def main():
    S = "1001100111"
    print(C(S))



main()