def T(numbers, target):
    l, r = 0, len(numbers)-1
    res = []
    while l<r:
        if numbers[l] + numbers[r] == target:
            res.append(l+1)
            res.append(r+1)
            l = r
        elif numbers[l] + numbers[r] < target:
            l+=1
        elif numbers[l] + numbers[r] > target:
            r-=1
    return res

def main():
    N = [2,7,11,15]
    print(T(N,9))
    N = [-1,0]
    print(T(N,-1))
    N = [1,2,3,4,5,6,7,8,9,10,11,20,30,50,61,90]
    print(T(N,35))


main()