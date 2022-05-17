class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

l=0
r=1
def T(original, cloned, target):
    
    if original == None:
        return None
    if original == target:
        return cloned
    return T(original.left, cloned.left, target) or T(original.right, cloned.right, target)



def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr


def main():
    P=TreeNode(3)
    T_ins(P,l,1)
    T_ins(P,r,4)
    N=P.left
    T_ins(N,r,2)
    N = P
    R= P.right

    print(T(P,N,R))

main()

