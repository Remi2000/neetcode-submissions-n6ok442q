"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_map = {}

        def dfs(old_node):
            if old_node in clone_map:
                return clone_map[old_node]

            clone_map[old_node] = Node(old_node.val)
            new_node = clone_map[old_node]

            for nei in old_node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node

        return dfs(node)