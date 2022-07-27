class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr
    

def Pre(ro):
    res = []
    if ro == None:
        return []
    else:
        L=Pre(ro.left)
        R=Pre(ro.right)
        res.append(ro.val)
        res = res+L+R
    return res

    
def main():

    P = TreeNode(1)
    T_ins(P,l,2)
    T_ins(P,r,5)
    N = P.left
    T_ins(N,l,3)
    T_ins(N,r,4)
    N = P.right
    T_ins(N,r,6)

    print(Pre(P))
    res=Pre(P)
    rr = P
    for i in range(1,len(res)):
        cur = TreeNode(res[i])
        rr.right = cur
        rr = rr.right
    P.left = None




main()