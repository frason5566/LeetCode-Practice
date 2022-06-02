class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def M(head):
    cnt = 0
    current = head
    while current != None :
        current = current.next
        cnt += 1
    m = cnt // 2
    print(cnt)
    print(m)
    current = head
    cnt = 0
    while cnt < m :
        current = current.next
        cnt += 1
    return current
        


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
    L1=ListNode(1)
    N_ins(L1,2)
    N_ins(L1,3)
    N_ins(L1,4)
    N_ins(L1,5)
    N_ins(L1,6)
    N_ins(L1,6)
    print("L1 = ",end='')
    N_Dis(L1)
    N_Dis(M(L1))

main()

