def W(nums): # Linear DP
    up = [0 for i in range(len(nums))]
    dn = [0 for i in range(len(nums))]
    up[0] = dn[0] = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up[i] = dn[i-1] + 1
            dn[i] = dn[i-1]
        elif nums[i] < nums[i-1]:
            dn[i] = up[i-1] + 1
            up[i] = up[i-1]
        else:
            dn[i] = dn[i-1]
            up[i] = up[i-1]
    print(up)
    print(dn)
    return max(up[-1], dn[-1])

def WW(nums): # greedy 
    if len(nums) < 2: return len(nums)
    pd = nums[1] - nums[0]
    cnt = 2 if pd != 0 else 1
    for i in range(2,len(nums)):
        d = nums[i]-nums[i-1]
        if (d > 0 and pd <=0) or (d < 0 and pd >= 0):
            cnt += 1
            pd = d
    return cnt
    
def main():
    N = [3,3,3,2,4]
    print(WW(N))
    N = [1,17,5,10,13,15,10,5,16,8]
    print(WW(N))
    N = [0,0]
    print(WW(N))

main()