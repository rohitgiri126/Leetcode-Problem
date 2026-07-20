# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.summ=float("-inf")
        def dfs(root):
            if not root:
                return 0
            l=max(0,dfs(root.left))
            r=max(0,dfs(root.right))
            self.summ=max(self.summ,l+r+root.val)
            return root.val+max(l,r)
        dfs(root)
        return self.summ        