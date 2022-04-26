class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val > root.val:
        print("Correct")
        return root.val
    elif p.val < root.val and q.val < root.val:
        print("Left")
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        print("Right")
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root.val



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

    P=TreeNode(6)
    T_ins(P,l,2)
    T_ins(P,r,8)
    N=P.left
    T_ins(N,l,0)
    T_ins(N,r,4)
    Q=N.right
    T_ins(Q,l,3)
    T_ins(Q,r,5)
    N=P.right
    T_ins(N,l,7)
    T_ins(N,r,9)
    print(lowestCommonAncestor(P,TreeNode(2),TreeNode(4)))

main()