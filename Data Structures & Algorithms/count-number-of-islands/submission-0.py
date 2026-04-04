class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 时间复杂度 O(mn)
        # 空间复杂度 O(mn)
        visited = set()
        count = 0
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        
        row = len(grid)
        col = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                r, c = queue.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
            
        return count
        