def M (nums): # best
    return (len(nums) + 1) * len(nums) // 2 - sum(nums)

def MM(nums):
    for i in range(len(nums)+1):
        try:
            res = nums.index(i)
        except:
            return i

def main():
    N = [0,1,2,3,4,5,6,8,9]
    print(M(N))

main()