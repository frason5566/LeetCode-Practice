class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def T(root):
    def M(r):
        if r==None:
            return 0
        else :
            D = max(M(r.left),M(r.right))
            return 1 + D
    D = M(root)
    a=[]
    for i in range (D):
        a.append([])

    def TT(roo,le):
        if roo == None: 
            return
        else:
            a[le].append(roo.val)
            TT(roo.left, le+1)
            TT(roo.right, le+1)
    TT(root,0)
    return a
   

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
#         while R != None:


def main():
    N=P=TreeNode(3)
    T_ins(P,l,9)
    T_ins(P,r,30)
    N=P.right
    T_ins(N,l,15)
    T_ins(N,r,7)
    
    print(' ',P.val)
    N=P.left
    F=P.right
    print(N.val,' ',F.val)
    print("  ",F.left.val,'',F.right.val )

    print(T(P))

main()