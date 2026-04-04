class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 时间	O(V + E)	每个节点和边各访问一次
        # 空间	O(V + E)	邻接表 + visited + 递归栈
        # 建邻接表（无向图，两个方向都加）
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            # 标记当前节点已访问
            visited.add(node)
            # 遍历所有邻居，没访问过的就递归
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # 遍历每个节点，没访问过的就启动一次新的 DFS
        for i in range(n):
            if i not in visited:
                dfs(i)          # 一次 DFS = 一个连通分量
                count += 1

        return count