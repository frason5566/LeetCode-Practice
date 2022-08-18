from itertools import count

    
def R(arr):
    d = dict()
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    d =  {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    print(d)
    cnt = 0
    n = len(arr)
    for v in d:
        n -= d[v]
        cnt +=1
        if n<=len(arr)/2:
            return cnt
        





def main():
    A = [7,3,3,5,2,5,5,2,3,3]
    print(R(A))
    A = [7,7,7,7,7,7]
    print(R(A))
    A = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19,63]
    print(R(A))


main()