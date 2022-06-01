def hasAllCodes(s, k):
    if len(s) < k: return False
    res = set()
    for i in range(len(s)-k+1):
        res.add(s[i:i+k])
    if len(res) == 2**k: return True
    return False

def main():

    s='00110110'
    print(hasAllCodes(s,2))
    s='0110'
    print(hasAllCodes(s,1))


main()