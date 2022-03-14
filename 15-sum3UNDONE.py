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
    res = []
    if len(nums)<3: return []
    def find(a,layer,target):
        l = 0
        r = len(a)-1
        if layer == 2:
            List = []
            while l < r:
                if a[l] + a[r] == target:
                    List.append(a[l])
                    List.append(a[r])
                elif a[l] + a[r] > target:
                    r -= 1
                elif a[l] + a[r] < target:
                    l +=1
            return List
        else:
            find(a[1:],layer-1,target - a[0])

    for i in range(len(nums)):
        find(nums, 3, 0 - nums[i])

                    
        

     return res

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