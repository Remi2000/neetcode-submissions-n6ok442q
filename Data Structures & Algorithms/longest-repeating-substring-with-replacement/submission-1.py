from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            while left < right and ((right - left + 1) - max(freq.values()) > k):
                freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
 