def M(s):
    D = dict()
    m=[]
    for l in s:
        if l not in D:
            D[l] = 1
        else:
            D[l] += 1
    for k in D:
        m.append(D[k])
    m.sort(reverse = True)

    cnt = 0
    maxA = m[0]
    for i in range(1,len(m)):
        if m[i] >= maxA :
            cnt += m[i] - maxA + 1
            m[i] = maxA - 1
        maxA = m[i] if m[i] > 0 else 1
        print(m)
    return cnt

def MM(s):
    D = dict()
    m = []
    cnt = 0
    for l in s:
        if l not in D:
            D[l] = 1
        else:
            D[l] += 1
    for k in D:
        if D[k] not in m:
            m.append(D[k])
        else:
            tmp = D[k]
            while tmp in m and tmp != 0:
                tmp -= 1
                cnt += 1
            m.append(tmp)
        
    return cnt


def main():
    S = 'ceabaacb'
    print(M(S))
    S = 'bbcebab'
    print(M(S))
    S = 'aaabbbcccddd'
    print(M(S))

main()