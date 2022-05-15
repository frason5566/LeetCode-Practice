def C(nums, target): # too slow
    nums.sort()
    for i in range(len(nums)):
        if nums[i]>target:
            nums = nums[0:i]
            break
    if len(nums) == 0: return 0
    res = 0
    def helper(N,T):
        nonlocal res
        for item in N:
            if T-item == 0:
                res += 1
                # print(item)
                return
            elif T-item > 0:
                helper(N,T-item)
            elif T-item < 0:
                return
    
    helper(nums,target)

    return res

def CC(nums, target):
    nums.sort()
    nums = set(nums)
    dp = [0] * (target+1) 
    dp[0] = 1
    for i in range(1,len(dp)):
        for j in range(i+1):
            if j in nums:
                dp[i] += dp[i-j]
    return dp[target]

def main():
    N = [1,2,3]
    print(CC(N,4))
    N = [3,2,1]
    print(C(N,5))
    N = [1,2,4]
    print(C(N,32))
    N = [9]
    print(C(N,3))

main()