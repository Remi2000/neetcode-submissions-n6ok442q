class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 时间	O(m × n)	每个格子最多被两次 DFS 各访问一次
        # 空间	O(m × n)	两个 visited 集合 + 递归栈
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        for i in range(m - 1, -1, -1):
            dfs(i, n - 1, atlantic)
        for j in range(n - 1, -1, -1):
            dfs(m - 1, j, atlantic)

        
        return list(pacific & atlantic)