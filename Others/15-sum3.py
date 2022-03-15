def T(nums): # Nest 
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
    res = []
    if len(nums)<3: return []
    nums.sort()
    def find(a,target):
        if len(a)<2: return
        l=0
        r=len(a)-1
        while  l < r:
            sum1 = target + a[l] + a[r]
            if sum1 == 0:
                res.append([target,a[l],a[r]])
                l+=1
                while a[l] == a[l-1] and l < r:
                    l += 1
            elif sum1 < 0:
                l+=1
            else:
                r-=1
            
    for i in range(len(nums)):
        if  i > 0 and nums[i]== nums[i-1]: continue
        find(nums[i+1:], nums[i])

    return res

def TTT(nums): # Set soultion, not fast
    output = set()
    nums.sort()
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                output.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return output

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