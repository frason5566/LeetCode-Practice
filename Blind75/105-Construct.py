class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def C(preorder,inorder):
    if not preorder or not inorder:
        return None
    res = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    res.left = C(preorder[1:mid+1],inorder[:mid])
    res.right = C(preorder[mid+1:],inorder[mid+1:])
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

    P = [3,9,20,15,7]
    I = [9,3,15,20,7]
    root = C(P, I)
    print(root.val)
    print(root.left.val, root.right.val)

main()