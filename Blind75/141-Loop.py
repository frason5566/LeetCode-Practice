class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Lo(head):

    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

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
    L=ListNode()
    N_ins(L,1)
    N_ins(L,2)
    N_ins(L,3)
    N_ins(L,4)
    current = L
    while current.next != None:
        current = current.next
    T=L
    T=T.next
    current.next = T
    print(Lo(L))

main()