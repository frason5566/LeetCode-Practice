def O (nums):
    res = ""
    if len(nums) == 1: res += str(nums[0])
    if len(nums) == 2: res =  str(nums[0]) + "/" + str(nums[1])
 
    return res

def main():

    L = [1000,100]
    print(O(L))
    L = [2]
    print(O(L))
main()