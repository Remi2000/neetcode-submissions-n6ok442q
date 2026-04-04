class Solution:

    def encode(self, strs: List[str]) -> str:
        # 时间复杂度：O(N)，N 是所有字符串总长度
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # 时间复杂度：O(N) 一共只会处理每个字符一次（扫描 + 切片）
        res = []
        i = 0

        while i < len(s):
            # 1. 从 i 开始往右找 '#'，锁定“长度数字”的区间 [i, j)
            j = i
            while s[j] != "#":      
                j += 1

            # 2. 解析长度
            length = int(s[i:j])

            # 3. 从 j+1 开始，取 length 个字符
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # 4. i 跳到下一个编码段的开头
            i = j + 1 + length

        return res