import heapq
class MedianFinder: # Slow
    def __init__IT(self):
        self.A = []
        self.m = 0
        self.t = 0

    def addNumIt(self, num: int) -> None:
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

    def findMedianIt(self) -> float:
        if self.t == 0:
            return (self.A[self.m-1]+self.A[self.m])/2
        else:
            return self.A[self.m]

    def __init__(self):
        self.min_heap = []  # store larger half
        self.max_heap = []  # store smaller half
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, - heapq.heappop(self.max_heap))
        if len(self.max_heap)<len(self.min_heap):
            heapq.heappush(self.max_heap, - heapq.heappop(self.min_heap))
        print(self.max_heap)
        print(self.min_heap)
        
    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return 0.5 * (-self.max_heap[0] + self.min_heap[0])
        else:
            return -self.max_heap[0]






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