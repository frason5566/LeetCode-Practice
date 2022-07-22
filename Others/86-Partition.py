
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def P(head, x):
    res = ListNode(0)
    temp = ListNode(0)
    prevR = res
    prevT = temp
    cur = head
    while cur != None:
        print(cur.val)
        if cur.val >= x:
            prevT.next = cur
            prevT = prevT.next
        else: 
            prevR.next = cur
            prevR = prevR.next
        cur = cur.next
    prevT.next = None
    prevR.next = temp.next
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
    current = H
    while current != None:
        print(current.val,",",end=" ")
        current = current.next
    print()


def main():
    L1=ListNode(1)
    N_ins(L1,4)
    N_ins(L1,3)
    N_ins(L1,2)
    N_ins(L1,5)
    N_ins(L1,2)
    N_Dis(L1)
    N_Dis(P(L1, 3))


main()
