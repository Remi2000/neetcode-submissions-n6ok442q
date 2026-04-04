class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 时间复杂度： O(n log n)（排序主导）
        # 空间复杂度： O(n)（用于存放结果）
        intervals.sort(key = lambda x: x[0])
        merge = [intervals[0]]

        for start, end in intervals[1:]:
            lastestEnd = merge[-1][1]
            if start <= lastestEnd:
                merge[-1][1] = max(lastestEnd, end)
            else:
                merge.append([start, end])
        return merge