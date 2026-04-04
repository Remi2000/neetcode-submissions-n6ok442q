class Solution:
    def trap(self, height: List[int]) -> int:
        # 方法	        时间	空间	说明
        # 前缀/后缀数组	O(n)	O(n)	三遍遍历 + 两个额外数组
        n = len(height)
        if n == 0:
            return 0

        # 预计算每个位置左边的最高柱子
        max_left = [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        # 预计算每个位置右边的最高柱子
        max_right = [0] * n
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        # 每个位置的水量 = min(左边最高, 右边最高) - 自己的高度
        water = 0
        for i in range(n):
            level = min(max_left[i], max_right[i])
            if level > height[i]:
                water += level - height[i]

        # water += max(0, min(max_left[i], max_right[i]) - height[i])

        return water