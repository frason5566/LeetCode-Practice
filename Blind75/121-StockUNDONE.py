def S (prices):
    maxP = 0
    for i in range (len(prices)-1):
        if prices[i] >= prices[i+1]: continue
        for j in range (len(prices)-1,i,-1):
            if prices[j] <= prices[j-1]: continue
            p = prices[j] - prices[i]
            if p > maxP:
                maxP = p
    return maxP

def SS(prices):
    if len(prices) == 1 : return 0
    a=prices.copy()
    a.sort()
    l = 0
    r = len(a)-1
    while l < r:
        



def main():
    L = [7,5,1,4,3,9,5,2]
    L = [7,8,9,1,1,2,4]
    print(SS(L))
main()