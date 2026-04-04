class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0

        repect = set()

        for r in range(len(s)):
            # 因为重复可能发生在更右边的位置，只删除一次删不完全比如"pwwkew" 但是left-> p, rihgt-> 第二个w的情况
            # 假如现在窗口是"pww"，删除一次只删掉了p，重复的w还在
            while s[r] in repect:
                repect.remove(s[l])
                l += 1
            repect.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
