class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 时间    O(n²)   枚举 n 个中心，每次扩展最多 O(n)
        # 空间    O(1)    只用了常数个变量，不计输出本身
        res = ""
        max_len = 0

        # 奇数长度：以 s[i] 为中心向两边扩展
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        # 偶数长度：以 s[i] 和 s[i+1] 之间为中心向两边扩展
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res