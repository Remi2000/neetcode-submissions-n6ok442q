class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            # 当前位置超过了我能到达的最远距离，走不到这里
            if i > max_reach:
                return False

            # 更新最远能到达的位置
            max_reach = max(max_reach, i + nums[i])

        return True
