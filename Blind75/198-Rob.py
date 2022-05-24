def R(nums):
    a, b = 0, nums[0]
    for i in range(1, len(nums)):
        print("i =",i,", num[i] =", nums[i])
        a, b = b, max(b, a+nums[i])
        print(a,",",b)
        
    return b

def main():
    N= [1,3,2,7,3]
    print(R(N))
    N = [2,1,3,9,7,3,1]
    print(R(N))


main()