import heapq

def T(nums,k):
    dict_={}
    for item in nums:
        if item not in dict_:
            dict_[item]=1
        else:
            dict_[item] += 1
    res = []
    heapq.heapify(res)
    for key,val in dict_.items():
        heapq.heappush(res,(val,key))
        print(res)
        if len(res) > k:
            heapq.heappop(res)

    return [key[1]for key in res]


def main():

    A=[1,1,1,1,2,2,3,4,4,4]
    print(T(A,3))

main()