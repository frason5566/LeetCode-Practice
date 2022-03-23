from sys import maxsize


def M(nums):
    if len(nums)==1: return nums[0]
    MaxS = nums[0] 
    for i in range (len(nums)):
        res = nums[i]
        if res > MaxS:
            MaxS = res
        for j in range(i+1,len(nums)):
            res *= nums[j]
            if res > MaxS:
                MaxS = res
        
    return MaxS
    
    
    
def MM(nums):
    if len(nums)==1: return nums[0]
    res = nums[0]
    MaxP = MaxN = nums[0]
    for item in nums[1:]:
        temp = MaxP * item
        MaxP = max(MaxP * item, item, MaxN * item)
        MaxN = min(temp, item, MaxN * item)
        if res < MaxP:
            res = MaxP
    return res

    


def MMM(nums):
    n = len(nums)
    local_max = nums[0]
    global_max = nums[0]
    local_min = nums[0]
    
    for i in range(1, n):
        temp = nums[i]*local_max
        print("temp = ",temp)
        local_max = max(local_max*nums[i], nums[i], local_min*nums[i])
        local_min = min(local_min*nums[i], nums[i], temp)
        print("local Max = ",local_max)
        print("local Min = ",local_min)
        if local_max > global_max:
            global_max = local_max
    
    return global_max


def main():
    N=[-3,0,1,-2]
    print(MM(N))
    N=[-2,1,-3,4,-1,2,1,5,-9,-1,4,10]
    print(MM(N))
    # N=[-2,-1]
    # print(M(N))
main()