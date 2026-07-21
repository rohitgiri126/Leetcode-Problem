from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        dq = deque([root])
        left_to_right = True
        
        while dq:
            lq = len(dq)
            level = []
            
            for _ in range(lq):
                node = dq.popleft()
                level.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
           
            if not left_to_right:
                level.reverse()
                
            ans.append(level)
            left_to_right = not left_to_right  
        return ans