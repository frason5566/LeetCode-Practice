class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def M(lists):
    res=ListNode()
    ll=len(lists)
    if ll == 0: return res
    elif ll == 1: return lists[0]
    C=[None]*ll
    ch = 0
    for i in range (ll):
        if lists[i]!=None:
            C[i]=lists[i]
            ch += 1
    if ch == 0 :return res
    T=res
    Flag = True
    while Flag:
        Flag=False
        ptr=ListNode()
        ptr.next=None
        minN=float("inf")
        minI=0
        for i in range(len(C)):
            if C[i] == None:
                continue
            elif C[i].val<=minN:
                minN = C[i].val
                ptr.val=C[i].val
                minI=i
            elif C[i].val < C[i-1].val:
                pt=ListNode()
                pt=C[i]
                C[i]=C[i-1]
                C[i-1]=pt
        T.next = ptr
        C[minI] = C[minI].next
        T = T.next
        for i in range(len(C)):
            if C[i]!=None:
                Flag = True
    return res

def MM (lists):
    res = head = ListNode()
    ll=len(lists)
    a=[]
    if ll == 0: return res
    elif ll == 1: return lists[0]
    for L in lists:
        while L != None:
            a.append(L.val)
            L=L.next
    a.sort()
    for N in a:
        ptr=ListNode()
        ptr.val=N
        res.next=ptr
        res = res.next
    return head


def N_ins(H,v):
    ptr = ListNode()
    ptr.next = None 
    ptr.val = v

    prev = H
    current = H.next
    
    while current != None :
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
    
def N_Dis(H):
    if H.next == None:
        print()
    else:
        current = H.next
        while current != None:
            print(current.val,",",end=" ")
            current = current.next
        print()

def main():
    L1=ListNode()
    N_ins(L1,1)
    N_ins(L1,2)
    N_ins(L1,8)
    print("L1 = ",end='')
    N_Dis(L1)
    L1=L1.next
    L2=ListNode()
    N_ins(L2,4)
    N_ins(L2,5)
    N_ins(L2,9)
    print("L2 = ",end='')
    N_Dis(L2)
    L2=L2.next
    L3=ListNode()
    N_ins(L3,3)
    N_ins(L3,6)
    N_ins(L3,7)
    print("L3 = ",end='')
    N_Dis(L3)
    L3=L3.next
    A=[L1,L3,L2]
    N_Dis(MM(A))


main()