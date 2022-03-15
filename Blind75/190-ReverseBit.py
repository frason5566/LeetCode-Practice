def R (n): # Not fast
    res = 0
    for i in range(32):
        res *= 2
        res += n % 2
        n = n // 2
    return res

def RR(n):
    source = bin(n)[2:]
    res = 0
    r = len(source)-1
    for i in range(len(source)-1,-1,-1):
        res *= 2
        if source[i] == "1":
            res +=1
    if r != 32: 
        res *= (2 ** (31-r))
    return res

def main():
    N = 43261596 # 00000010100101000001111010011100
    print("N = 00000010100101000001111010011100,",43261596,". Reverse into")
    print(RR(N))
main()