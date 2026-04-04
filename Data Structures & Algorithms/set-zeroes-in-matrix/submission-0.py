class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 时间	O(m × n)	两遍扫描矩阵，每遍 O(m × n)
        # 空间	O(m + n)	两个标记数组，分别长 m 和 n
        m, n = len(matrix), len(matrix[0])
        
        # 两个标记数组：记录哪些行/列需要清零
        row_zero = [False] * m
        col_zero = [False] * n

        # 第一遍：扫描矩阵，遇到 0 就标记它所在的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True

        # 第二遍：根据标记统一清零
        for i in range(m):
            for j in range(n):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0

        