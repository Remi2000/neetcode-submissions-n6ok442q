class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(filtered) - 1
        while left < right:
            if filtered[left] == filtered[right]:
                left += 1
                right -= 1
            else:
                return False
        return True