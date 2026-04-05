class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 时间    O(n³)   外层两个循环 O(n²)，双指针 O(n)
        # 空间    O(1)    不计输出数组
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # 跳过第一层重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # 跳过第二层重复
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # 跳过双指针层重复
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res