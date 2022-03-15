def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    List = []
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                List.append(i)
                List.append(j)
    return List

def T(nums, target): # Fatser solution
    List = []
    a=nums.copy()
    
    nums.sort()
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            List.append(a.index(nums[l]))
            if nums[l] != nums[r]:
                List.append(a.index(nums[r]))
            else:
                List.append(a.index(nums[r],a.index(nums[l])+1))
            l=r
        elif nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l +=1
    return List

def main():
    L = [1,2,3,4,5,6,7,8,9,1]
    t = 12
    print(T(L,t))


main()