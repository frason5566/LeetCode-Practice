class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def M(root):
    res = -float("INF")
    def dfs(ro):
        nonlocal res
        if not ro:
            return 0
        else:
            l = max(0,dfs(ro.left))
            r = max(0,dfs(ro.right))
            res = max(res, ro.val+l+r)
            return ro.val+(max(l,r))

        
    return max(dfs(root),res)


def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr
    
def main():
    N=P=TreeNode(-10)
    T_ins(P,l,9)
    T_ins(P,r,20)
    N=P.right
    T_ins(N,l,15)
    T_ins(N,r,7)
    print(M(P))

main()