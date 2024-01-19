# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=collections.deque()
        q.append(root)
        level=[]
        levels=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()              
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levels.append(sum(level)/len(level))
        return levels