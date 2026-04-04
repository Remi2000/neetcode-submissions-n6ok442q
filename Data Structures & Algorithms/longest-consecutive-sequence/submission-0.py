class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # 1️⃣ 把所有元素放进 set，支持 O(1) 查找
        numsSet = set(nums)
        maxLen = 0

        # 2️⃣ 遍历每个数，只有在它是“连续序列开头”时才扩展
        for n in numsSet:
            # 如果 n-1 不在集合里，说明 n 是某个连续段的起点
            if n - 1 not in numsSet:
                curr = n
                curLen = 1

                # 一直往右找：n+1, n+2, ...
                while curr + 1 in numsSet:
                    curr += 1
                    curLen += 1

                maxLen = max(maxLen, curLen)

        return maxLen
