def F(nums, k):
    nums.sort(reverse = True)
    print(nums)
    return nums[k-1]


def main():


    N = [3,2,1,5,6,4]
    print(F(N,4))


main()