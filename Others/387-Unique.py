def U(s):
    a = dict()
    for i in range(len(s)):
        if s[i] not in a:
            a[s[i]] = 1
        else:
            a[s[i]] += 1
    for i in range(len(s)):
        if a[s[i]] == 1:
            return i
    return -1

def main():
    S='leetcode'
    print(U(S))
    S='loveleetcode'
    print(U(S))
    S='aabb'
    print(U(S))


main()


