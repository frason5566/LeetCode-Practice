def M(nums):
    if len(nums)==1: return nums[0]
    maxS = res = nums[0]
    for item in nums[1:]:
        res+=item
        if res<item:
            res = item
        if maxS<res:
            maxS = res
    return maxS


def main():
    # N=[1,2,3,4]
    # print(M(N))
    N=[-2,1,-3,4,-1,2,1,5,-9,-1,4,10]
    print(M(N))
    # N=[-2,-1]
    # print(M(N))
main()