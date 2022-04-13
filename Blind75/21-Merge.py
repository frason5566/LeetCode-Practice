class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def M(list1,list2): # on VSCode
    prev=list1
    C1=list1
    C2=list2
    while C1 != None or C2 != None:
        if C1 == None :
            prev.next = C2
            C2 = C2.next

        elif C2 == None:
            C1 = C1.next

        elif C1.val<=C2.val:
            prev = C1
            C1 = C1.next

        elif C1.val > C2.val:
            temp = ListNode()
            temp.val = C2.val
            temp.next = None
            prev.next = temp
            temp.next = C1
            C2 = C2.next
    return list1

def MM(list1,list2): # on leetcode
    res = ListNode()
    C1=list1
    C2=list2
    T=res
    while C1 != None or C2 != None:
        ptr=ListNode()
        ptr.next=None
        
        if C1 == None:
            T.next = C2
            C2 = C2.next

        elif C2 == None:
            T.next = C1
            C1 = C1.next

        elif C1.val<=C2.val:
            ptr.val=C1.val
            T.next=ptr
            C1 = C1.next

        elif C1.val > C2.val:
            ptr.val=C2.val
            T.next=ptr
            C2 = C2.next
        T = T.next
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
    L2=ListNode()
    N_ins(L2,1)
    N_ins(L2,3)
    N_ins(L2,6)
    print("L2 = ",end='')
    N_Dis(L2)
    N_Dis(MM(L1,L2))

main()


