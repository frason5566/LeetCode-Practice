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
        print(m)
        if nums[r] < nums[m] :
            l = m + 1
        else:
            r = m 
    return nums[m]

def main():
    N=[6,7,0,1,2]
    print(FF(N))
    N=[11,13,15,17]
    print(FF(N))
    N=[3,4,5,1,2]
    print(FF(N))
    0,1,2,3,4
    4,0,1,2,3
    3,4,0,1,2
    2,3,4,0,1
    1,2,3,4,0

main()