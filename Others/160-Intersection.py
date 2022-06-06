class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def I(headA, headB):
    A = headA
    s = set()
    while A != None:
        s.add(A)
        A = A.next
    A = headB
    while A:
        if A in s:
            return A
        A = A.next
    return None


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
    current = H
    while current != None:
        print(current.val,",",end=" ")
        current = current.next
    print()

def main():
    L1=ListNode(4)
    N_ins(L1,1)
    L2=ListNode(5)
    N_ins(L2,6)
    N_ins(L2,1)
    L3=ListNode(8)    
    N_ins(L3,4)
    N_ins(L3,5)
    c = L1
    while c.next != None:
        c = c.next
    c.next = L3
    c = L2
    while c.next != None:
        c = c.next
    c.next = L3
    print("L1 = ",end='')
    N_Dis(L1)
    print("L2 = ",end='')
    N_Dis(L2)
    N_Dis(I(L1, L2))

main()

