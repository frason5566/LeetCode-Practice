def R(nums, x):
    N = sum(nums) - x
    if N == 0: return len(nums)
    print(N)
    cur = 0
    res = 0
    found = False
    start = 0
    for i in range(len(nums)):
        cur += nums[i]
        while cur > N and start < i:
            cur -= nums[start]
            start += 1
        if cur == N:
            res = max(res, i - start + 1)
            found = True
    if found:
        return len(nums) - res
    return -1


def main():
    N = [1,1,4,2,3]
    print(R(N,5))
    N = [5,6,7,8,9]
    print(R(N,4))
    N = [3,2,20,1,1,3]
    print(R(N,10))
    N = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
    print(R(N,134365))

main()