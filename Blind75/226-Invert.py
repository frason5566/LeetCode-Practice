class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def I(root):
    if root == None: return root
    elif root.left == None and root.right == None: return root
    else:
        ptr=root.left
        root.left = I(root.right)
        root.right = I(ptr)
        return root


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
    print(P.val)
    N=P.left
    F=P.right
    print(N.val,' ',F.val)
    F=F.right
    print(F.val)
    P=I(P)
    print(P.val)
    N=P.left
    F=P.right
    print(N.val,' ',F.val)
    F=F.right
    print(F.val)



main()