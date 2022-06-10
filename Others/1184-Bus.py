def B(distance, start, destination):
    S = sum(distance)
    if start > destination:
        start, destination = destination, start
    mi = 0
    for i in range(start,destination):
        mi += distance[i]

    return min(mi, S-mi)

def BB(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    mi = 0
    for i in range(start,destination):
        mi += distance[i]
    ma = 0
    for i in range(start):
        ma += distance[i]
    for i in range(destination, len(distance)):
        ma += distance[i]
    return min(mi,ma)

def main():

    N = [1,2,3,4]
    print(BB(N,0,2))
    N = [1,2,3,4,1,2,3]
    print(BB(N,2,5))

main()