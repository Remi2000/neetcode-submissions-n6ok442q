class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 时间复杂度 O(n) 桶排序虽然看起来有两层 for，但内层遍历的是“所有元素总共跑一遍”，不是 “对每个 i 再跑一遍 n 次”，
        # 空间复杂度 O(n)
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if not freq[i]:
                continue
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res