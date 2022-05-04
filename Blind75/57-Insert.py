def MMM(intervals,newInterval):
    intervals.append(newInterval)
    s = sorted([i[0] for i in intervals])        
    e = sorted([i[1] for i in intervals])
    res = []
    fp = s[0]
    i = 0
    while i<(len(s)-1):
        if e[i]>=s[i+1]:
            i+=1
            continue
        res.append([fp,e[i]])
        fp = s[i+1]
        i+=1
    res.append([fp,e[-1]])
    return res


def main():
    I = [[1,3],[6,9]]
    print(MMM(I,[2,5]))
    I = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    print(MMM(I,[4,8]))

main()