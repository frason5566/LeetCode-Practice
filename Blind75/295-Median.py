class MedianFinder: # Slow
    def __init__(self):
        self.A = []
        self.m = 0
        self.t = 0

    def addNum(self, num: int) -> None:
        if len(self.A) == 0:
            self.A.append(num)
        else:
            if num >= self.A[self.m]:
                for i in range(self.m,len(self.A)):
                    if num > self.A[i]:
                        if i == len(self.A)-1:
                            self.A.append(num)
                        else:
                            continue
                    elif num <= self.A[i]:
                        self.A.insert(i,num)
                        break
            elif num < self.A[self.m]:
                for i in range(self.m+1):
                    if num > self.A[i]:
                        if i == self.m:
                            self.A.insert(self.m-1,num)
                        else:
                            continue
                    elif num <= self.A[i]:
                        self.A.insert(i,num)
                        break
        self.m += self.t
        self.t = 1 if self.t == 0 else 0
        print(self.A)

    def findMedian(self) -> float:
        if self.t == 0:
            return (self.A[self.m-1]+self.A[self.m])/2
        else:
            return self.A[self.m]





def main():
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())

main()