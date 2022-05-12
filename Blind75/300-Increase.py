def I (nums):
    # helper = [float("-INF") for i in range(len(nums))]
    count = [1  for i in range(len(nums)) ]
    L=len(nums)
    for i in range(L-1,-1,-1):
        for j in range(i+1,L):
            if nums[i] < nums[j]:
                count[i] = max(count[i],count[j]+1)
    res = max(count)
    return res



def main():
    N = [10,9,2,5,3,7,101,18]
    print(I(N))
    # N = [0,1,0,3,2,3]
    # print(I(N))
    # N = [7,7,7,7,7,7]
    # print(I(N))
    # N = [4,10,4,3,8,9]
    # print(I(N))

main()