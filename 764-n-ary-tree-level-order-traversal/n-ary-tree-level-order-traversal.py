from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        dq = deque([root])
        
        while dq:
            lq = len(dq)
            level = []
            
            for _ in range(lq):
                node = dq.popleft()
                level.append(node.val)
                
                if node.children:
                    for child in node.children:
                        dq.append(child)
            
            ans.append(level)
            
        return ans