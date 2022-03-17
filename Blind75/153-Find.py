def F(nums):
    res = nums[0]
    for i in range(1,len(nums)):
        if nums[i]>res:continue
        else :res = nums[i]
    return res

def FF(nums):
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return nums[0] if nums[0] < nums[1] else nums[1]
    l=0
    r=len(nums)-1

    while l < r:
        m = (l+r) // 2
        print("l =",l,",r =",r,",m =",m)
        if nums[m] > nums[r] or (r == l+1 and nums[l]>nums[r]):
            l = m + 1 
        else:
            r = m
    
    return nums[l] if nums[l]<nums[r] else nums[r]

def main():
    N=[0,1,2,3,4]
    print(FF(N))
    N=[4,0,1,2,3]
    print(FF(N))
    N=[3,4,0,1,2]
    print(FF(N))
    N=[2,3,4,0,1]
    print(FF(N))
    N=[1,2,3,4,0]
    print(FF(N))

main()