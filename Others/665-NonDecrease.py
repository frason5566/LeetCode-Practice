def D(nums):
    if len(nums) == 1: return True
   
    cnt = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            cnt +=1
            if i >= 2 and nums[i-2]> nums[i]:
                nums[i] = nums [i-1]
        if cnt >=2:
            return False

    return True


def main():
    N = [4,2,3]
    print(D(N))
    N = [4,2,1]
    print(D(N))
    N = [1,2,3,4,4,4,4,5,6,5,8,9]
    print(D(N))
    N = [3,4,2,3]
    print(D(N))
    N = [5,7,1,8]

main()
