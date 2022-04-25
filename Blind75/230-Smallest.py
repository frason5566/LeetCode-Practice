class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def S(root,k):
    def T(root): # preorder
        res = []
        if root == None:
            return []
        else:
            L=T(root.left)
            R=T(root.right)
            res.append(root.val)
            res = L+res+R
        return res
    A=T(root)
    return A[k-1]


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
    N=P=TreeNode(5)
    T_ins(P,l,3)
    T_ins(P,r,6)
    N=P.left
    T_ins(N,l,2)
    T_ins(N,r,4)
    R=N.left
    T_ins(R,l,1)

    print(S(P))

main()