def S(nums,target):
    res = [-1,-1]
    for i in range(len(nums)):
        if res[0] == -1 and nums[i] == target:
            res[0] = i
        elif res[0] != -1 and nums[i] == target:
            res[1] = i
        if res[0] != -1 and i ==len(nums)-1 and res[1] == -1:
            res[1]=i
    return res

def SS(nums, target):
    # res = [-1, -1]
    l,r = 0, len(nums)-1
    while nums[l] != target and l < r:
        l += 1
    if l == r and nums[r] != target:
        return [-1,-1]
    while nums[r] != target:
        r -= 1
    return [l, r]

def main():
    N=[1,2,3,3,4,5,6,7,8,8,8,9]
    print(SS(N,8))
    print(SS(N,10))
    print(SS(N,9))


main()