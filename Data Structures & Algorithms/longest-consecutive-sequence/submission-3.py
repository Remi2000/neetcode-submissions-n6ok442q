class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        all_nums = set(nums)
        max_len = 1

        for n in nums:
            length = 1
            if n - 1 in all_nums:
                continue
            else:
                nxt = n + 1
                while nxt in all_nums:
                    length += 1
                    nxt += 1
                max_len = max(max_len, length)
        
        return max_len