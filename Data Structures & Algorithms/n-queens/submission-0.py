class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()     # 记录被占用的列
        diag1 = set()    # 记录主对角线 (row - col)
        diag2 = set()    # 记录副对角线 (row + col)

        def backtrack(row: int) -> None:
            # row == n：说明 0..n-1 行都成功放好了
            if row == n:
                res.append(["".join(r) for r in board])
                return

            # 尝试在当前 row 的每一列放皇后
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # 冲突就跳过

                # 做选择：放皇后
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # 递归下一行
                backtrack(row + 1)

                # 回溯：撤销选择
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
