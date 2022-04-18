class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def R(head): # List
    current = head
    A=[]
    while current!= None:
        A.append(current.val)
        current = current.next
    # print(A)
    res = ListNode()
    l,r = 0, len(A)-1
    T = res
    while l <= r:
        if l != r :
            # print(1)
            ptr = ListNode()
            ptr.val = A[l]
            T.next = ptr
            T=T.next
            ptr2 = ListNode()
            ptr2.val = A[r]
            T.next = ptr2
            T=T.next
        elif l == r:
            # print(2)
            ptr = ListNode()
            ptr.val = A[l]
            T.next = ptr
        l+=1
        r-=1
    head.next=res.next.next

def RR(head): # ListNode
    c1=head
    prev=head
    c1=c1.next
    while c1.next != None:
        ptr=ListNode()
        c2=head
        while c2.next!=None:
            p2 = c2
            c2 = c2.next
        p2.next=None
        ptr.val=c2.val
        

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
    N_ins(L1,3)
    N_ins(L1,4)
    N_ins(L1,5)
    # N_Dis(RR(L1))
    R(L1.next)
    # R(L1)
    N_Dis(L1)



main()