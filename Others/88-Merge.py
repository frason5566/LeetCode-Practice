def M(nums1,m,nums2,n):
    if m == 0: 
        for i in range(n):
            nums1[i] = nums2[i]
        return
    if n == 0: return
    print(len(nums1))
    print(len(nums2))
    a = m-1
    b = n-1
    for i in range(m+n-1,-1,-1):
        if a < 0:
            nums1[i] = nums2[b]
            b -= 1
        elif b < 0:
            nums1[i] = nums1[a]
            a -= 1
        elif nums1[a]>nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1
    


def MM(nums1,m,nums2,n):
    nums1[m:] = nums2
    nums1.sort()

def main():
    # N1 = [1,2,3,0,0,0]
    # N2 = [2,5,6]
    # M(N1,3,N2,3)
    # print(N1)
    N1 = [-12,-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    N2 = [-17,-16,-15,-14,-13,-11,-10,-9,0,0,0,1,2,3,4]
    M(N1,2,N2,15)
    print(N1)

main()