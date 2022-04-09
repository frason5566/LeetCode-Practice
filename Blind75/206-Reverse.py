class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def R(head):  # iteratively 
    res = ListNode()
    res.next = None
    current = head
    current = current.next
    while current != None:
        ptr = ListNode()
        ptr.next = None
        ptr.val = current.val
        prev = res.next
        res.next = ptr
        ptr.next = prev
        current = current.next

    return res

count = 0
def RR(head): # recursively
    global count
    if head.next == None:
        # print("core")
        # print(head.val)
        return head
    else:
        # count +=1
        # print("head = ",head.val,"count = ",count)
        recur = RR(head.next)
        ptr = ListNode()
        ptr.val= head.next.val
        ptr.next = None
        prev = recur
        current = recur.next
        while current != None:
            prev = current
            current = current.next
        prev.next = ptr

        return recur

def RRR(head):
    def Rev(N,H):
        if H == None:
            return N
        else:
            print(H.val)
            NewH = H.next
            H.next = N
            NH = H
            return Rev(NH,NewH)
    return Rev(None, head)

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
    H=ListNode()
    N_ins(H,1)
    N_ins(H,2)
    N_ins(H,3)
    N_ins(H,5)
    N_Dis(RRR(H))
    
main()