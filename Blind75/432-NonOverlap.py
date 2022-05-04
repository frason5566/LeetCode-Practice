def N(intervals):
   
    intervals.sort(key = lambda x: x[0])
    overlap_c = 0
    last_end = intervals[0][1]
    for start,end in intervals[1:]:
        if last_end > start:
            overlap_c +=1
            last_end = min(last_end,end)
        else:
            last_end = end
    return overlap_c


def main():
    I = [[1,3],[6,9]]
    print(N(I))
    I = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    print(N(I))
    I = [[1,2],[2,3],[3,4],[1,3]]
    print(N(I))
    I = [[1,2],[1,2],[1,2]]
    print(N(I))

main()