def P(words, pattern):
    p = dict()
    cnt = 0
    pat = []
    res = []
    for l in pattern:
        if l not in p:
            p[l] = cnt
            cnt += 1
        pat.append(p[l])
    # print(temp)
    for word in words:
        cnt = 0
        wp = dict()
        wpat = []
        for l in word:
            if l not in wp:
                wp[l] = cnt
                cnt += 1
            wpat.append(wp[l])
        if wpat == pat:
            res.append(word)
        
    return res


def main():
    W = ['bee', 'abc', 'mee', 'app', 'klp', 'hiv']
    print(P(W, 'abb'))
    W = ['a', 'b', 'c']
    print(P(W, 'a'))


main()
