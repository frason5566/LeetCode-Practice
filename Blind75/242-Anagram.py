def A(s,t):
    if len(s)!= len(t): return False
    sletters = dict()
    tletters = dict()
    for i  in range(len(s)):
        if s[i] not in sletters:
            sletters[s[i]] = 1
        elif s[i]  in sletters:
            sletters[s[i]] += 1
        if t[i] not in tletters:
            tletters[t[i]] = 1
        elif t[i]  in tletters:
            tletters[t[i]] += 1
    if len(sletters) != len(tletters): return False
    for item in sletters:
        if item not in tletters:
            return False
        elif sletters[item] != tletters[item]:
            return False
    return True

def AA(s,t): #not good
    if len(s)!= len(t): return False
    sl = []
    tl = []
    for i in range(len(s)):
        sl.append(s[i])
        tl.append(t[i])
    sl.sort()
    tl.sort()
    return sl == tl

def main():
    S="anagram"
    T="nagaram"
    print(AA(S,T)) 
    S="cat"
    T="rat"
    print(AA(S,T))



main()