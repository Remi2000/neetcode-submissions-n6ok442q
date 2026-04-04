"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # 时间复杂度	O(V + E)	DFS 会访问每个节点一次（V），处理每条边一次（E）
    # 空间复杂度	O(V)	clone_map 保存所有节点映射；DFS 递归栈最深为 O(V)
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 如果整个图为空，直接返回 None
        if not node:
            return None

        # 哈希表：记录旧节点 -> 新节点 的映射关系
        # 作用：
        # 1. 避免重复克隆节点
        # 2. 处理图中的环（cycle）
        clone_map = {}

        def dfs(old_node):
            # 如果这个旧节点已经克隆过，直接返回对应的新节点
            # 防止环导致无限递归
            if old_node in clone_map:
                return clone_map[old_node]

            # 第一次遇到旧节点：先 clone 出对应的新节点（只有 val）
            clone_map[old_node] = Node(old_node.val)
            new_node = clone_map[old_node]

            # 再克隆所有邻居，并加入 new_node.neighbors
            for nei in old_node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node  # 返回克隆好的新节点

        # 从输入 node 开始 DFS 克隆整个图
        return dfs(node)