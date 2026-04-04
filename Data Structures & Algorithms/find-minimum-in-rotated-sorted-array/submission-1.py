class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 时间复杂度	O(log n)	每次把搜索区间缩小一半
        # 空间复杂度	O(1)	只用到了常数个变量
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
        