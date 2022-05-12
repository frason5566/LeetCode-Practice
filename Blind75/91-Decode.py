def D(s):
    if s[0]=='0':return 0
    res = 0
    L = len(s)
    nums=[]
    count=[]
    for i in range(L):
        nums.append(int(s[i]))
    for i in range(0,L-1):
        if nums[i]!=0:
            res += 1
            count.append(nums[i])
            N = nums[i] * 10 + nums[i+1]
            if N <= 26:
                res += 1
                count.append(N)

    print(count)
    if nums[L-1]!=0 : res += 1
    return res

def main():

    S = "12"
    print(D(S))
    S = "226"
    print(D(S))
    S = "06"
    print(D(S))
    S = "111222"
    print(D(S))

main()