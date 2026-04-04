class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited_path = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != word[idx]
                or (r, c) in visited_path):
                return False

            visited_path.add((r, c))

            res = (dfs(r + 1, c, idx + 1) 
                    or dfs(r - 1, c, idx + 1) 
                    or dfs(r, c + 1, idx + 1) 
                    or dfs(r, c - 1, idx + 1))

            visited_path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

            