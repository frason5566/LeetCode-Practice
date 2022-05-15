class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def L(root):
    def helper(r,l):
        if r == None: return 0
        if r.left == None and r.right == None:
            return l
        else:
            return max(helper(r.left, l+1), helper(r.right, l+1))
    level = helper(root,0)
    res = 0
    def helper2(r,l):
        if r == None:
            return 0
        elif l < level:
            return helper2(r.left, l+1) + helper2(r.right, l+1)
        elif l == level:
            return r.val
        else: return 0
    res = helper2(root, 0)
    return res



def LL(root):
    end = []
    res = 0
    def helper(r,l):
        if r == None: return 0
        if r.left == None and r.right == None:
            end.append([l,r.val])
        else:
            helper(r.left, l+1)
            helper(r.right, l+1)
    helper(root,0)
    level = 0
    # print(end)
    for item in end:
        # print(item[0])
        if item[0] > level:
            res = item[1]
            level = item [0]
        elif item[0] == level:
            res += item[1] 
    return res




def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr
    
def main():
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

    print(LL(P))

main()
