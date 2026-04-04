class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 时间	O(n)	三个 while 加起来每个区间只看一次
        # 空间	O(n)	result 数组存所有区间
        result = []
        i = 0
        n = len(intervals)

        # 第一阶段：当前区间完全在 newInterval 前面，直接加入
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 第二阶段：当前区间和 newInterval 有重叠，不断合并
        start = newInterval[0]
        end = newInterval[1]
        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        result.append([start, end])

        # 第三阶段：当前区间完全在 newInterval 后面，直接加入
        while i < n:
            result.append(intervals[i])
            i += 1

        return result