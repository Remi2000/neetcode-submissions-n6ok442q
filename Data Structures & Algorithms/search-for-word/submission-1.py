from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # 记录当前这条搜索路径上已经访问过的坐标，防止重复使用同一个格子
        visited_path = set()

        def dfs(r: int, c: int, idx: int) -> bool:
            """
            从坐标 (r, c) 开始，尝试匹配 word[idx:]
            如果能从这里一直匹配到单词末尾，则返回 True
            """

            # ✅ 成功条件：已经匹配完 word 的所有字符
            if idx == len(word):
                return True

            # ❌ 失败 / 非法情况：越界、字符不匹配、或者当前格子已在路径中
            if (r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != word[idx]
                or (r, c) in visited_path):
                return False

            # 做选择：标记当前格子已访问
            visited_path.add((r, c))

            # 在四个方向继续匹配下一个字符
            res = (
                dfs(r + 1, c, idx + 1) or  # 下
                dfs(r - 1, c, idx + 1) or  # 上
                dfs(r, c + 1, idx + 1) or  # 右
                dfs(r, c - 1, idx + 1)     # 左
            )

            # 撤销选择：回溯，把当前格子从路径中移除
            visited_path.remove((r, c))

            return res

        # 尝试每一个格子作为起点，去匹配 word[0]
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        # 所有起点都试过了都不行，返回 False
        return False
