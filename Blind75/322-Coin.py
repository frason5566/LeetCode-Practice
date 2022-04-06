def C(coins,amount):
    a=[amount+1]*(amount+1)
    a[0]=0
    for i in range(len(a)):
        for coin in coins:
            if coin <= i:
                a[i] = min(a[i], a[i-coin]+1)
    return a[amount] if a[amount] < amount+1 else -1
   

def main():

    cc=[1,2,5]
    A=11
    print(C(cc,A))
    cc=[1,5,10]
    A=11
    print(C(cc,A))
    cc=[1,9]
    A=11
    print(C(cc,A))
    cc=[5,10]
    A=11
    print(C(cc,A))

main()