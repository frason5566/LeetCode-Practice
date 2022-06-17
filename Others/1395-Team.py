def T(rating):
    T = 0
    for i in range(1,len(rating)):
        lh,ll = 0,0
        rh,rl = 0,0
        for j in range(i):
            if rating[j] < rating[i]:
                ll +=1
            if rating[j] > rating[i]:
                lh +=1
        for j in range(i+1, len(rating)):
            if rating[j] < rating[i]:
                rl +=1
            if rating[j] > rating[i]:
                rh +=1
        T += ll*rh + lh*rl
    return T
def main():
    t = [2,5,3,4,1]
    print(T(t))

main()