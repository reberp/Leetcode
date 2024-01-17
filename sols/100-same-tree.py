# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if (not p and q) or (not q and p):
                return False
            elif (not q and not p):
                return True
            elif ((not p.left and q.left) or (p.left and not q.left) or 
                (not p.right and q.right) or (p.right and not q.right)):
                return False
            if (
                (p.val != q.val) or
                (not p.left and q.left) or
                (not q.left and p.left) or
                not isSame(p.left,q.left) or 
                not isSame(p.right,q.right)):
                return False
            return True
        if not p and not q:
            return True
        if not p or not q:
            return False
        return isSame(p,q) and isSame(p.left,q.left) and isSame(p.right,q.right)