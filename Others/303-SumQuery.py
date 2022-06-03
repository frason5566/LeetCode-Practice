class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.dp=[]
        self.dp.append(self.nums[0])
        for i in range(1, len(self.nums)):
            self.dp.append(self.dp[i-1] + self.nums[i])
        print(self.dp)
    def sumRange(self, left, right):
        if left > 0:
            return self.dp[right] - self.dp[left-1]
        else:
            return self.dp[right]



def main():

    N=[1,2,3,4,5,6,7,8,9]
    A = NumArray(N)
    print(A.sumRange(2,5))

main()
