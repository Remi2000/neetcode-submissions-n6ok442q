from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 时间复杂度	O(n)	左右指针各最多遍历字符串一次
        # 空间复杂度	O(1)	频率表最多 26 个字符（常数空间）
        
        freq = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        