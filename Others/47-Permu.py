def P(nums):
    if len(nums) == 1 : return [nums]
    def helper(N):
        if len(N) == 2:
            if N[0]==N[1]:
                return [[N[0],N[1]]]
            return [[N[0],N[1]],[N[1],N[0]]]
        if len(N) > 2:
            res = []
            for i in range(len(N)):
                print(i)
                if N[i] not in N[:i] or i == 0:
                    temp = N[0:i] + N[i+1:len(N)]
                    print(temp)
                    re = helper(temp)
                    for item in re:
                        # print(item)
                        r=[N[i]]
                        r.extend(item)
                        # print(r)
                        res.append(r)
                    # res.append()
            return res
    
    return helper(nums)


def main():

    N=[1,1,2]
    print(P(N))
    N = [1,1,1,4,5]
    print(P(N))

main()