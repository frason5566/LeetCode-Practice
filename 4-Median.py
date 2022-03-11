def M (nums1,nums2):
    N = nums1 + nums2
    if len(N)==1: return N[0]
    flag = 0
    while flag == 0:
        flag = 1
        for i in range(len(N)-1):
            if N[i]>N[i+1]:
                N[i],N[i+1] = N[i+1],N[i]
                flag = 0
    # print(N)
    if len(N) % 2 == 0:
        m = int(len(N)/2)
        # print("m = ", m)
        return (N[m] + N[m-1])/2
    elif len(N) % 2 == 1:
        m = int((len(N)-1)/2)
        return N[m]

def K(nums1,nums2):

    N = nums1+nums2
    j = 0
    k = 0
    for i in range (len(nums1)+len(nums2)):
        if j>=len(nums1):
            N[i] = nums2[k]
            k += 1 if k<len(nums2) else 0
        elif k>=len(nums2):
            N[i] = nums1[j]
            j += 1 if j<len(nums1) else 0
        elif nums1[j] <= nums2[k]:
            N[i] = nums1[j]
            j += 1 if j<len(nums1) else 0
        else:
            N[i] = nums2[k]
            k += 1 if k<len(nums2) else 0
    if len(N)==1: return N[0]
    if len(N) % 2 == 0:
        m = int(len(N)/2)
        return (N[m] + N[m-1])/2
    elif len(N) % 2 == 1:
        m = int((len(N)-1)/2)
        return N[m]



def main():
    N1=[1,2,3]
    N2=[-5,-1]
    print(K(N1,N2))
    N1=[1,2]
    N2=[3,4]
    print(K(N1,N2))
    N1=[1,2,3]
    N2=[-5,-1,4]
    print(K(N1,N2))
    N1=[]
    N2=[-5,-1]
    print(K(N1,N2))


main()