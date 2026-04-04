class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 时间复杂度	O(n²)
        # 空间复杂度	O(1)（原地操作）
        
        n = len(matrix)

        # Step 1: 转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: 反转每一行
        for row in matrix:
            row.reverse()

        