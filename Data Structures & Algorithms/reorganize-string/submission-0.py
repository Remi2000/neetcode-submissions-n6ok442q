import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # 时间    O(n log k)n     是字符串长度，k 是不同字符数（最多26），每次堆操作 O(log k)
        # 空间    O(k)            堆的大小最多 k 个字符
        count = Counter(s)
        max_heap = []

        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))

        res = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if not res or res[-1] != char:
                res += char
                if freq + 1 != 0:
                    heapq.heappush(max_heap, (freq + 1, char))
            
            else:
                # 和上一个相同，先取第二高的
                # 能进 else，说明 char1 和 res[-1] 相同，也就是当前频率最高的字符和上一个放的一样，必须先放别的字符。
                # 但此时 max_heap 空了，意味着只剩这一种字符了，而它又不能紧接着放，那后面无论怎么排都会相邻冲突。
                if not max_heap:
                    return ""
                freq2, char2 = heapq.heappop(max_heap)
                res += char2
                if freq2 + 1 != 0:
                    heapq.heappush(max_heap, (freq2 + 1, char2))
                heapq.heappush(max_heap, (freq, char))

        return res