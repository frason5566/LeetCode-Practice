def T(nums):
    if len(nums)<3: return []
    if len(nums)==3:
        if nums[0]+nums[1]+nums[2]==0:
            return [nums]
    res = []
    flag = 0
    nums.sort()
    # print(nums)
    for i in range (len(nums)):
        # if i > 0 and nums[i] == nums[i-1] : continue
        for j in range(i+1, len(nums)):
            target = 0 - nums[i] - nums[j]
            if target in nums[j+1:]:
                ok=[nums[i],nums[j],nums[nums.index(target)]]
                if ok not in res:
                    res.append(ok)
    return res

def TT(nums):
    if len(nums)<3: return []
    
    nums.sort()
    print(nums)
    def find(N,source,target,res,res_f):
        ress = []
        if N == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res_f.append(res + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1; r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
                    
        

     

def main():
    S = [-1,0,1,2,-1,-4]
    print(TT(S))
    # S = [0,0,0]
    # print(TT(S))
    # S = [0,0,0,0]
    # print(TT(S))
    S = [-2,1,-1,3,-2,-3,2,1]
    print(TT(S))

main()