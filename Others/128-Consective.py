def C(nums): 
    if len(nums) == 0:
        return 0
    nums.sort()
    crt = 1
    res = 1
    for i in range(1,len(nums)):
        # print(nums[i])
        if nums[i] == nums[i-1]+1:
            crt +=1
        elif nums[i] == nums[i-1]:
            continue
        else:
            res = max(crt,res)
            crt = 1
        res = max(crt,res)
    return res

def CC(nums): # Time O(n)
    if len(nums) == 0:
        return 0
    num_set = set(nums)
    res = 1
    for num in num_set:
        if num-1 not in num_set:
            cur = num
            crt = 1
            while cur + 1 in num_set:
                crt += 1
                cur += 1
            res = max(res, crt)
    return res

def main():
    N = [1,100,500,2,4,3]
    print(CC(N))
    N = [0,3,7,2,5,8,4,6,0,1]
    print(CC(N))
    N = [1,2,0,1]
    print(CC(N))
main()