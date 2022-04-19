class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def M(root):
    if root==None:
        return 0
    else :
        D = max(M(root.left),M(root.right))
        return 1 + D


def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr
    
# def T_Dis(R):
#     if R == None:
#         print()
#     else:
#         D = M(R)
#         ptr = TreeNode()
#         for i in range (D):
#             print()


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

    print(M(P))

main()