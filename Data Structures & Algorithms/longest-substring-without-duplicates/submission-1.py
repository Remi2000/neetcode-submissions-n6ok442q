class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        r = 0
        dup = set()
        
        while l <= r < len(s):
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            count = max(count, r - l + 1)

            r += 1

        return count

