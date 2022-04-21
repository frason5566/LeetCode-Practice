class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def S(root,subRoot):
    def check(r,sr):
        if r == None and sr == None:
            return True
        elif r != None and sr != None:
            if r.val == sr.val:
                return check(r.left,sr.left) and check(r.right,sr.right)
            else:
                return False
        else:
            return False

    def find(N,sbb):
        if N == None:
            return False
        elif check(N,sbb):
            return True
        else:
            return find(N.left,sbb) or find(N.right,sbb)
    return find(root,subRoot)


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
    R=TreeNode(30)
    T_ins(R,l,15)
    T_ins(R,r,7)
    print(R)
    print(P.right)

    # print(P.val)
    # N=P.left
    # F=P.right
    # print(N.val,' ',F.val)
    # F=F.right
    # print(F.val)

    print(S(P,R))

main()