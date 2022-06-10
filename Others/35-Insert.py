def I(nums, target):
    if target in nums:
        return nums.index(target)
    l, r = 0, len(nums)-1
    while True:
        if nums[l] > target:
            return l
        if nums[r] < target:
            return r+1
        l+=1
        r-=1

def II(nums, target):
    if target in nums:
        return nums.index(target)
    nums.append(target)
    nums.sort()
    return nums.index(target)

def main():
    N = [1,2,3,4]
    print(I(N, 5))
    N = [1,2,3,4,6,8,9]
    print(I(N, 7))
    N = [1,2,3,4]
    print(I(N, 3))

main()