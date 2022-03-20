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
        if nums[m] == target:
            res = m
            l=r
        elif nums[l] == target:
            res = l
            l=r
        elif nums[r] == target:
            res = r
            l=r
        elif nums[m] < target:
            if nums[r] > target or nums[r] < nums[m]:
                l = m + 1
            elif nums[r] == target:
                res = r
                break
            else:
                r = m - 1
        elif nums[m] > target:
            if nums[l] < target or nums[l] > nums[m]:
                r = m - 1
            elif nums[l] == target:
                res = l
                break
            else:
                l = m + 1
    return res


def main():
    # N=[0,1,2,3,4,5]
    # print(SS(N,4))
    # N=[5,0,1,2,3,4]
    # print(SS(N,4))
    # N=[4,5,0,1,2,3]
    # print(SS(N,4))
    # N=[3,4,5,0,1,2]
    # print(SS(N,4))
    # N=[2,3,4,5,0,1]
    # print(SS(N,4))
    # N=[1,2,3,4,5,0]
    # print(SS(N,4))
    
    N=[3,1]
    print(SS(N,1))
    N=[3,1]
    print(SS(N,3))

main()