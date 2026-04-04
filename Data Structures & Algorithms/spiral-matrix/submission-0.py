class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 时间	O(m × n)
        # 空间	O(1)（不算输出）
        if not matrix:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1️⃣ left → right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2️⃣ top → bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3️⃣ right → left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # 4️⃣ bottom → top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res