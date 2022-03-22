class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbersL(l1, l2): # List Solution
    temp = 0
    List = []
    flag = 1
    i = 0
    s = 0
    while flag == 1:    
        if i >= len(l1) and i >= len(l2):
            if temp ==1:
                List.append(1)
            flag = 0
        else:
            if i < len(l1) and i < len(l2):
                s = l1[i] + l2[i] + temp
            elif i < len(l1) and i >= len(l2):
                s  = l1[i] + temp
            elif i >= len(l1) and i < len(l2):
                s  = l2[i] + temp
            if s >= 10:
                s -= 10
                temp = 1
            else:
                temp = 0
            List.append(s)
        
            i += 1
    return List

def addTwoNumbers(l1,l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1==None: return l2
    if l2==None: return l1
    
    res = ListNode(0)
    result = res
    s = 0
    carry = 0
    digit = 0
    flag = 1

    while flag:
        if l1 == None and l2 == None:
            if carry:
                result.next = ListNode(carry)
                result = result.next
                carry = 0
                flag = 0
        else:
            V1 = l1.val if l1 else 0
            V2 = l2.val if l2 else 0
            s = V1 + V2 + carry 
            carry = s // 10
            digit = s % 10
            result.next = ListNode(digit)
            result = result.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        
    return res.next




def main():
    
    l1 = ListNode(0)
    l1.val = 9
    l1.next = ListNode()
    l1.next = 4
    l2 = ListNode(0)
    l2 = [2,1,3,5]
    print(l1.val)
    print(l1.next)


main()