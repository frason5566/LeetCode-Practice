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
    low = prices[0]
    prf=0
    for i in range (1,len(prices)):
        if low>prices[i]:
            low = prices[i]
        if prices[i] - low > prf:
            prf = prices[i] - low 
    return prf
        



def main():
    L = [7,5,1,4,3,9,5,2]
    L = [7,8,9,1,1,2,4]
    print(SS(L))
main()