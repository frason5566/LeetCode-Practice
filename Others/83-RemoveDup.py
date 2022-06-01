class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def R(head):
    if head == None: return None
    if head.next == None: return head
    res = ListNode(head.val)
    ptr = res
    current = head.next
    while current != None:
        if current.val > ptr.val:
            ptr.next = ListNode(current.val)
            ptr = ptr.next
        current = current.next
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
        current = H
        while current != None:
            print(current.val,",",end=" ")
            current = current.next
        print()

def main():
    L1=ListNode()
    N_ins(L1,1)
    N_ins(L1,2)
    print("L1 = ",end='')
    N_Dis(L1)
    N_Dis(R(L1.next))

main()

