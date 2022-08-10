class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(self, nums):
    if not nums: return None
    m = len(nums)//2
    return TreeNode(nums[m], sortedArrayToBST(nums[:m]), sortedArrayToBST(nums[m+1:]))

l=0
r=1

def T_ins(R,D,v):
    ptr = TreeNode(v)
    prev = R
    if D == l:
        prev.left = ptr
    else:
        prev.right = ptr

def main():
    A = [-10,-3,0,5,9]
    print(sortedArrayToBST(A))


main()