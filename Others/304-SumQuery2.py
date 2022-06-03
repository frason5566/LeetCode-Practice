class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])
        self.dp = [[0] * n for i in range(m)]
        self.dp[0][0] = self.matrix[0][0]
        # print (self.dp)
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + self.matrix[i][0]

        for j in range(1, n):
            self.dp[0][j] = self.dp[0][j-1] + self.matrix[0][j]

        for y in range(1, m):
            for x in range(1, n):
                self.dp[y][x] = self.matrix[y][x] + self.dp[y-1][x] + self.dp[y][x-1] - self.dp[y-1][x-1]

        print(self.dp)

    def sumRegion(self, row1, col1, row2, col2) :
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        if row1 == 0 and col1 != 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        if row1 != 0 and col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]

    def sumRegion2(self, row1, col1, row2, col2) :
        sum = 0
        for x in range(col1, col2 + 1):
            for y in range(row1, row2 + 1):
                sum += self.matrix[y][x]
        return sum


def main():
    M = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    A = NumMatrix(M)
    print(A.sumRegion(0,0,0,0))
    print(A.sumRegion2(0,0,0,0))

main()