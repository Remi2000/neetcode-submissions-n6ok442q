class Solution:
    def reverse(self, x: int) -> int:
        # 时间复杂度	O(k) ≈ O(1)	处理整数的每一位，最多 10 位
        # 空间复杂度	O(1)
        # 32-bit 有符号整数的范围
        INT_MAX = 2**31 - 1    #  2147483647
        INT_MIN = -2**31       # -2147483648

        # 记录符号并把 x 转成正数处理
        sign = 1 if x >= 0 else -1
        x = abs(x)

        res = 0  # 反转后的数字

        # 不断取出 x 的末位数字
        while x:
            digit = x % 10   # 弹出最后一位
            x = x // 10      # x 去掉最后一位

            # 溢出检查（严格 32 位 检查）
            # 反转前要提前判断 res * 10 + digit 是否溢出
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            # 加入当前 digit 到结果末尾
            res = res * 10 + digit

        # 加回符号
        return sign * res