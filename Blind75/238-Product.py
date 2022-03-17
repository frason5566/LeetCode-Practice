def P(nums):
    n=len(nums)
    res=[0] * n
    l=[1] * n
    r=[1] * n
    for i in range (1,n):
        l[i] = l[i-1] * nums[i-1]
    res[n-1]= l[n-1]
    for i in range(n-2,-1,-1):
        r[i] = r[i+1] * nums[i+1]
        res[i] = r[i] * l[i]
    return res

def PP(nums):
    n=len(nums)
    res=[1] * n
    temp = 1
    for i in range (1,n):
        res[i] = res[i-1] * nums[i-1]
    for i in range(n-2,-1,-1):
        temp*= nums[i+1]
        res[i] *= temp

    return res

def main():
    N=[-1,1,0,-3,3]
    print(PP(N))
    N=[1,2,3,4]
    print(PP(N))
    N=[2,3,4,5]
    print(PP(N))
    N=[-1,-2,-3,-4]
    print(PP(N))

main()