def S(nums,target):
    if target not in nums: return -1
    if len(nums) == 1: return 0 
    res = -1
    l = 0
    r = len(nums)-1
    m = 0
    while m != res:
        m = (l+r) //2
        if nums[m] == target:
            res = m 
        elif target in nums[l:m+1]:
            r = m 
            res = m if len(nums[l:m+1]) == 1 else -1
        else:
            l = m + 1  
            res = m if len(nums[m:r+1]) == 1 else -1
    return res

def SS(nums,target):
    if len(nums)==1: return -1 if nums[0] != target else 0
    res = -1
    l = 0
    r = len(nums)-1
    m = (l+r)//2
    while l<r:
        m = (l+r)//2
        print("m=",m,",nums[m]=",nums[m])
        if nums[m] == target or nums[r]==target:
            res = m if nums[m] == target else r
            l=r
        elif nums[m] < target and target < nums[r]:
            l = m + 1
        elif nums[m] < target:
            r = m
        elif nums[m] > target and target < nums[l]:
            l = m+1
        else:    
            r = m
        
    return res


def main():
    # N=[4,5,6,7,0,1,2]
    # print(SS(N,0))
    # N=[4,5,6,7,0,1,2]
    # print(SS(N,3))
    N=[1,3]
    print(SS(N,3))
    N=[1,3]
    print(SS(N,1))
    # N=[1]
    # print(SS(N,0))
    # N=[0,1,2,3,4]
    # print(S(N,2))
    # N=[4,0,1,2,3]
    # print(S(N,2))
    # N=[3,4,0,1,2]
    # print(S(N,2))
    # N=[2,3,4,0,1]
    # print(S(N,0))
    # N=[1,2,3,4,0]
    # print(S(N,2))

main()