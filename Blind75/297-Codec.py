class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l=0
r=1

def serialize(root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    a=[]
    def TT(roo):
        if roo == None:
            a.append("N")
        else:
            a.append(str(roo.val))
            TT(roo.left)
            TT(roo.right)
    TT(root)
    return ",".join(a)
    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    a = data.split(",")
    
    ptr = TreeNode()


def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr


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


    print(serialize(P))

main()