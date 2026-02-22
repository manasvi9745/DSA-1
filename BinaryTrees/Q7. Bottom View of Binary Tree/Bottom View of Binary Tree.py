'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        # Dictionary to store horizontal distance -> node value
        hd_map = {}
        
        # Queue for BFS: (node, horizontal distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Overwrite value for bottom view
            hd_map[hd] = node.data
            
            if node.left:
                queue.append((node.left, hd - 1))
            
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Sort by horizontal distance
        sorted_hd = sorted(hd_map.keys())
        
        return [hd_map[hd] for hd in sorted_hd]
