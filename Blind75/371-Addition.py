def A(a,b): # bad
    if a == 0: return b
    if b == 0: return a
    if a * b > 0:
        aa=[1]*abs(a)
        bb=[1]*abs(b)
        aa.extend(bb)
        return len(aa) if a>0 else -len(aa)
    else:
        if abs(a) > abs(b):
            aa=[1]*abs(a)
            bb=[1]*abs(b)
            del aa[0:len(bb)]
            return len(aa) if a > 0 else -len(aa)
        else:
            aa=[1]*abs(a)
            bb=[1]*abs(b)
            del bb[0:len(aa)]
            return len(bb) if b > 0 else -len(bb)

def AA(a, b):
    if a == 0: return b
    if b == 0: return a
    res = []
    if a * b > 0:
        for i in range(abs(a)):
            res.append(1)
        for i in range(abs(b)):
            res.append(1)
        return len(res) if a > 0 else -len(res)
    else:
        if abs(a) > abs(b):
            for i in range(abs(a)):
                res.append(1)
            for i in range(abs(b)):
                res.pop()
            return len(res) if a > 0 else -len(res)
        else:
            for i in range(abs(b)):
                res.append(1)
            for i in range(abs(a)):
                res.pop()
            return -len(res) if a > 0 else len(res)



def main():

    print(AA(1,2))
    print(AA(-30,2))
    print(AA(1,-2))
    print(AA(-3,-2))

main()