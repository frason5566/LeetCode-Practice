def M(height):
    maxA = 0
    for i in range (len(height)):
        for j in range(i,len(height)):
            res = height[i] * (j-i) if height[i]<=height[j] else height[j] * (j-i)
            if res > maxA:
                maxA = res
    return maxA

def MM(height):
    maxA = 0
    l=0
    r=len(height)-1
    while l<r:
        res = height[l] * (r-l) if height[l]<=height[r] else height[r] * (r-l)
        if maxA < res: maxA = res
        if height[l]<height[r]:
            l+=1
        else: r-=1
    return maxA

def main():

    A = [1,8,6,2,5,4,8,3,7]
    print(MM(A))
    B = [1,1]
    print(MM(B))

main()