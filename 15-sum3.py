def T(nums):
    if len(nums)<3: return []
     
    res = []
    flag = 0
    nums.sort()
    for i in range (len(nums)):
        if nums[i] == nums[i-1] : continue
        for j in range(i+1, len(nums)):
            target = 0 - nums[i] -nums[j]
            if target in nums[j+1:]:
                ok=[nums[i],nums[j],nums[nums.index(target)]]
                if ok not in res:
                    res.append(ok)
    return res

def main():
    S = [-1,-1,2,3,4,5,-2]
    print(T(S))
    S = []
    print(T(S))
    S = [0,0,0]
    print(T(S))
    S = [-2,1,-1,3,-2,-3,2,1]
    print(T(S))

main()