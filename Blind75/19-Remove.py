class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def R(head, n):
    a=[]
    while head != None:
        a.append(head.val)
        head = head.next
    print(a)
    res = T = ListNode()
    for i in range (len(a)):
        
        if i != len(a)-n:
            ptr=ListNode(a[i])
            T.next=ptr
            T = T.next
        else:
            continue
    return res

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
    # R(L1)
    N_Dis(R(L1.next,3))

main()