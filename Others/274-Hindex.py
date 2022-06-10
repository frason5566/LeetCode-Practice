def H(citations):
    citations.sort(reverse = True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return len(citations)


def main():
    C = [3,0,6,1,5]
    print(H(C))
    C = [3,0,6,1,5,50,40,90,50,10,30,20,10,10,50,5,6,7,8,9,20,1,0,31,51,21,0,0,0,0,0,0,0]
    print(H(C))

main()

