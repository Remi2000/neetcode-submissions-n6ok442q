class Solution:
    def rob(self, nums: List[int]) -> int:
        # 时间复杂度  O(n)    遍历一次 nums
        # 空间复杂度  O(1)    只用了两个变量，无额外数组
        n = len(nums)

        if n == 1:
            return nums[0]
            
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # 抢这个房子 vs 跳过这个房子
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]