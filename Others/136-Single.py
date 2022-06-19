def S(nums):
    D = dict()
    for i in range(len(nums)):
        if nums[i] not in D:
            D[nums[i]] = 1
        else:
            D[nums[i]] +=1
    for item in D:
        if D[item] == 1:
            return item

def SS(nums):
    res = 0
    for num in nums:
        res ^= num
        print(res)
    return res
def main():
    N = [1,3,2,1,2,3,4]
    print(SS(N))


main()