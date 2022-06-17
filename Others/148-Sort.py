class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def S(head): # Time Limit Exceeded
    res = ListNode(float("-INF"))
    prev = head
    c = head.next
    cr = res
    
    while c != None:
        if prev.val > c.val:
            ins = ListNode(c.val)
            pr = res
            cc = res.next
            while cc != None:
                if ins.val > cc.val:
                    cc = cc.next
                    pr = pr.next
                else:
                    break
            pr.next = ins
            ins.next = cc
            
            prev.next = c.next
            c = c.next
        else: 
            prev = prev.next
            c = c.next
    prev = res
    cr = res.next
    c = head
    
    while c != None:
        if cr == None:
            prev.next = c
            break
        elif c.val < cr.val:
            ins = ListNode(c.val)
            prev.next = ins
            ins.next = cr
            prev = prev.next
            c = c.next
        else:
            prev = prev.next
            cr = cr.next
    return res.next

def SS(head):
    res = ListNode(float("-INF"))
    temp = []
    c = head
    while c != None:
        temp.append(c.val)
        c = c.next
    temp.sort()
    print(temp)
    cc = res
    for val in temp:
        cc.next = ListNode(val)
        cc = cc.next


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
    L1=ListNode(4)
    N_ins(L1,2)
    N_ins(L1,1)
    N_ins(L1,3)
    N_Dis(L1)
    N_Dis(SS(L1))

main()

