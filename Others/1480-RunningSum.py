def R(nums):
    if len(nums) == 1: return nums
    res = []
    res.append(nums[0])
    for i in range(1, len(nums)):
        res.append(nums[i]+res[-1])
    return res

def RR(nums):
    if len(nums) == 1: return nums
    for i in range(1, len(nums)):
        nums[i]=(nums[i]+nums[i-1])
    return nums


def main():
    N=[1,2,3,4]
    print(RR(N))




main()


