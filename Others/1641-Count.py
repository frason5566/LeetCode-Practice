def C(n):
    a=[[1] * 5 for i in range(n)]
    for i in range(1,n):
        a[i][0] = 1
        for j in range(1,5):
            a[i][j]=a[i-1][j]+a[i][j-1]
    S = sum(a[n-1])        
    
    return S
def CC(n):
    a,e,i,o = 1,1,1,1
    ta,te,ti,to = 1,1,1,1
    for j in range(1,n): 
        o = to + 1
        i = ti + o
        e = te + i
        a = ta + e
        ta,te,ti,to = a,e,i,o
    return a+e+i+o+1


def main():

    print(CC(1))
    print(CC(2))
    print(CC(33))

main()
# 1, 5, 15,35
# 1, 4, 10,20
# 1, 3, 6, 10
# 1, 2, 3, 4
# 1, 1, 1, 1
# '''
# aaa,aae,aai,aao,aau
# aee,aei,aeo,aeu
# aii,aio,aiu
# aoo,aou
# auu
# ,
# eee,eei,eeo,eeu
# eii,eio,eiu
# eoo,eou
# euu
# ,
# iii,iio,iiu
# ioo,iou
# iuu
# ,
# ooooo,oooou
# ooouu
# oouuu
# ouuuu
# ,
# uuu
# '''