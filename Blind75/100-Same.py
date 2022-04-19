class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def S(p,q):
    if p == None and q == None: return True
    elif p != None and q != None:
        if p.val == q.val:
            B1=S(p.left,q.left)
            B2=S(p.right,q.right)
            return (B1 and B2)
        else:
            return False
    else:
        return False


def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr
    
def main():
    N=P=TreeNode(3)
    T_ins(P,l,9)
    T_ins(P,r,30)
    N=P.right
    T_ins(N,l,15)
    T_ins(N,r,7)
    print(S(P,N))
    print(S(P,P))


main()