# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # def dfs(node):
        #     mr=0
        #     ml=0
        #     if not node: 
        #         return 0
        #     if not node.left and not node.right:
        #         return 1
        #     if node.left:
        #         ml = dfs(node.left)
        #     if node.right:
        #         mr = dfs(node.right)
        #     return 1+max(ml,mr)

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
            