def O (nums):
    res = ""
    if len(nums) == 1: res += str(nums[0])
    elif len(nums) == 2: res =  str(nums[0]) + "/" + str(nums[1])
    else:
        res += str(nums[0])+ "/(" 
        for i in range(1,len(nums)-1):
            res += str(nums[i]) + "/"
        res += str(nums[len(nums)-1]) + ")"
    return res

def main():

    L = [1000,100]
    print(O(L))
    L = [2]
    print(O(L))
main()