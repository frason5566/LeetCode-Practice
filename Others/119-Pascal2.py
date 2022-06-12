def P(rowIndex):
    if rowIndex == 1: return [1]
    res = [[1],[1,1]]
    if rowIndex == 2: return [1,1]
    for i in range(2,rowIndex+1):
        temp = [0 for j in range(i+1)]
        temp[0] = temp[i] = 1
        for j in range(1,i):
            temp[j] = res[-1][j] + res[-1][j-1]
        res.append(temp)
        
    return res[rowIndex]

def main():
    print(P(5))
    print(P(7))


main()