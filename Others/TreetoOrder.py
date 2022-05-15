class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

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
    P=TreeNode(3)
    T_ins(P,l,1)
    T_ins(P,r,4)
    N=P.left
    T_ins(N,r,2)

    print(T(P))
    # T=[]
    # R=[1,2,3]
    # G=T+R
    # print(G)
    P = TreeNode(1)
    T_ins(P,l,2)
    T_ins(P,r,3)
    N = P.left
    T_ins(N,l,4)
    T_ins(N,r,5)
    N = N.left
    T_ins(N,l,7)
    N = P.right
    T_ins(N,r,6)
    N = N.right
    T_ins(N,r,8)

    print(T(P))

main()