def S(n):
    if n == 1: return 1
    A=[0]*(n+1)
    A[0]=A[1]=1
    for i in range(2,n+1):
        A[i]=A[i-2]+A[i-1]
    return A[n]

def SS(n):
    if n == 1: return 1
    A1=A2=1
    for i in range(2,n+1):
        Sum = A1 + A2
        A1 = A2
        A2 = Sum

    return Sum

def main():
    N=3
    print(S(N))
    N=4
    print(S(N))
    N=5
    print(S(N))
    N=6
    print(S(N))
    N=7
    print(S(N))





main()