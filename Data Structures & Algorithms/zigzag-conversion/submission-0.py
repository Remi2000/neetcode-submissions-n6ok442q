class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 时间    O(n)    每个字符只处理一次
        # 空间    O(n)    所有桶加起来存了 n 个字符
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ["" for _ in range(numRows)]
        curr_row = 0
        # 初始化为 -1：第一个字符放入 row=0 后触发翻转变成 1，才能正确向下走
        directions = -1

        for c in s:
            rows[curr_row] += c
            # 到达顶行或底行时翻转方向
            if curr_row == 0 or curr_row == numRows - 1:
                directions *= -1
            curr_row += directions
        
        return "".join(rows)