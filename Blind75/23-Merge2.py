class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def M(lists): 
    ll=len(lists)
    C=[ListNode()]*ll
    for i in range (ll-1):
        C[i]=lists[i]
    res=ListNode()
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
                print("i =", i , "Val =",C[i].val)
                ptr.val=C[i].val
                minI=i
        T.next = ptr
        print(type(C[minI]),"  ",minI)
        C[minI] = C[minI].next
        print("Next, C[minI].next = ",C[minI])
        T = T.next
        for i in range(len(C)):
            if C[i]!=None:
                Flag = True
    return res.next

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
    N_ins(L1,4)
    print("L1 = ",end='')
    N_Dis(L1)
    L1=L1.next
    L2=ListNode()
    N_ins(L2,5)
    N_ins(L2,8)
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
    A=[L1,L2,L3]
    N_Dis(M(A))
    A=[[],[],[]]
    print(A)

main()