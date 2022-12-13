def PP(n):
    a = [i for i in range(1, n+1)]
    for i in range(len(a)):
        if sum(a[:i]) == sum(a[i+1:]):
            return i+1
    return -1
def P(n):
    for x in range(1,n+1):
        B, C = x*(x+1)//2, (n-x+1)*(x+n)//2

        if B == C: return x
    return -1
            
            

def main():
    print(P(8))
    print(P(4))
    print(P(1))

main()