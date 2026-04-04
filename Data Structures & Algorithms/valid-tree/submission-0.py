class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 时间	O(V + E)	建图 O(E) + DFS 访问所有节点和边 O(V + E)
        # 空间	O(V + E)	邻接表 O(V+E) + visited 集合 O(V) + 递归栈 O(V)
        if len(edges) != (n - 1):
            return False

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == n

