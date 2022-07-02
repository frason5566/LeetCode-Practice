def M(nums):
    l = 0
    r = len(nums)-1
    res = 0
    while l < r:
        res += abs(nums[l] - nums[r])
        l += 1
        r -= 1
    return res

def MM(nums):
    res = 0
    tar = sorted (nums) [len(nums) // 2]
    for i in range(len(nums)):
        res += abs(nums[i] - tar)
    return res
    

def main():
    N = [1,10,1,2,129]
    print(MM(N))
    N = [1,10,2,2,129]
    print(MM(N))
    N = [1,10,3,2,129]
    print(MM(N))
    N = [1,10,4,2,129]
    print(MM(N))
    N = [1,10,5,2,129]
    print(MM(N))


main()