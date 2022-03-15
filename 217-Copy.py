def C(nums): # not good
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            continue
        else: return True
    return False

def CC (nums): # Bad
    if len(nums) == 1 :return False
    for i in range(len(nums)-1):
        print("i = ",i,", nums[i] = ",nums[i])
        try:
            a = nums.index(nums[i],i+1)
            print(a)
            return True
        except:
            continue
    return False

def CCC(nums): # Set solution
    test = set(nums)
    if len(nums) != len(test):
        return True
    else:
        return False

def CCCC(nums):
    
    return False

def main():

    L = [1,2,3,4,5,1]
    print(CC(L))
    L = [1,2,4,5]
    print(CC(L))
    L = [1,2,3,4,5,1,1,1]
    print(CC(L))
    L = [1,2,3,3]
    print(CC(L))
    # L = [1,2,3,4,1,5]
    # print(L.index(0,1))

main()