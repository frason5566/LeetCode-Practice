def R(s):
    if len(s) == 1:
        if s =='?':
            return 'a'
        else:
            return s

    res = ''
    if s[0] == '?':
        if s[1] =='a':
            res += 'b'
        else:
            res += 'a'
    else:
        res += s[0]
    for i in range(1,len(s)-1):
        if s[i] == '?':
            if res[i-1] == 'a' :
                if s[i+1] == 'a':
                    res += 'b'
                elif s[i+1] == 'b':
                    res += 'c'
                else:
                    res += 'b'
            elif res[i-1] == 'b' :
                if s[i+1] == 'b':
                    res += 'a'
                elif s[i+1] == 'a':
                    res += 'c'
                else:
                    res += 'a'
            else:
                if s[i+1] == 'a':
                    res += 'b'
                else :
                    res += 'a'
        else:
            res += s[i]

    if s[len(s)-1] == '?':
        if res[len(s)-2] == 'a' :
            res += 'b'
        else:
            res += 'a'
    else:
        res += s[len(s)-1]
    return res

def main():
    S = '?zs'
    print(R(S))
    S = '?z?s'
    print(R(S))
    S = "??yw?ipkj?"
    print(R(S))
    S = "alk??jah??as?ac?b??b??a"
    print(R(S))

main()