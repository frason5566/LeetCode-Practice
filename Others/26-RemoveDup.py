def R(nums):
    cnt = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            continue
        else:
            nums[cnt] = nums[i]
            cnt +=1
    # del nums[cnt:]  # method 1
    return cnt      # method 2