def S(matchsticks): # DFS Time O(n ** 4)
    if len(matchsticks) < 4: return False
    P = sum(matchsticks)
    if P % 4 != 0: return False
    l = P // 4
    matchsticks.sort(reverse=True)
    # print(matchsticks)
    # print(l)
    if matchsticks[0] > l:
        return False
    sums = [0 for i in range(4)]
    def dfs(index):
        if index == len(matchsticks):
            return sums[0] == sums[1] == sums[2] == l
        for i in range(4):
            if sums[i] + matchsticks[index] <= l:
                sums[i] += matchsticks[index]
                if dfs(index+1):
                    return True
                sums[i] -= matchsticks[index]
        return False
    return dfs(0)


def main():
    M = [3,3,3,3,4]
    print(S(M))
    M = [1,1,2,2,2]
    print(S(M))
    M = [1,2,3,4,5,6,7,8]
    print(S(M))
    M = [1,2,3,4,5,6,7,8,9,10,11,14]
    print(S(M))

main()