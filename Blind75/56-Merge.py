from operator import itemgetter
def M (intervals):
    if len(intervals) == 1: return intervals
    intervals.sort(key = itemgetter(0, 1))
    res = [intervals[0]]
    print(intervals)
    for i in range(1,len(intervals)):
        # start,end = start and end of current interval
        start=intervals[i][0]
        end=intervals[i][1]
        # if end of current interval overlaps with the end of the last interval in the merged list
        if start<=res[-1][1]:
            # update the end of last interval in the merged list
            res[-1][1]=max(end,res[-1][1])
        else:
            # else add the current interval in the merged list
            res.append([start,end])
    return res        

def MM(intervals):
    if len(intervals) == 1: return intervals

    ans = []
    start = []
    end = []
    for item in intervals:
        start.append(item[0])
        end.append(item[1])
    start.append(-float("Inf"))
    s = e = 0
    flag = 0
    
    while e < len(end):
        print("s =",s,", e =",e,", flag =",flag)
        if flag == 0:
            temp = [0]*2
            temp[0] = start[s]
            s += 1
            flag += 1
        elif flag > 0:
            if s >= len(start) or start[s] > end[e]:
                temp[1] = end[e]
                flag -= 1
                e += 1
                ans.append(temp)
                print(temp)
                print(ans)
            elif start[s] <= end[e]:
                s += 1
                flag += 1
    return ans

def MMM(intervals):
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
    # I = [[1,3],[4,6],[8,10],[15,18]]
    # print(MM(I))
    # I = [[1,5],[2,6],[8,23],[20,26]]
    # print(MM(I))
    # I = [[1,4],[5,6]]
    # print(MM(I))
    # I = [[1,4],[1,4]]
    # print(MM(I))
    I = [[1,3],[2,2],[2,3],[2,2],[5,9],[4,8]]
    print(MMM(I))

main()