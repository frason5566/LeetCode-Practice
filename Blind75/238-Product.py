def P(nums):
    res=[0]*len(nums)
    temp = 1
    zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        
    return res


def main():
    N=[-1,1,0,-3,3]
    print(P(N))
    N=[1,2,3,4]
    print(P(N))
    N=[2,3,4,5]
    print(P(N))
    N=[-1,-2,-3,-4]
    print(P(N))

main()