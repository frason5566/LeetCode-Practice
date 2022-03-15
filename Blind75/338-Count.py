def C(n):
    if n == 0: return [0]
    res = [0] * (n+1)
    
    return res

def main():
    n=8
    print(C(n))
    n=10
    print(C(n))

main()