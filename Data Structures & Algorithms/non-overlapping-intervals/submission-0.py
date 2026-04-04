class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 时间	O(n log n)	排序 O(n log n) + 遍历 O(n)
        # 空间	O(1)	只用了 count 和 prev_end 两个变量
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # 重叠：删掉当前这个（它 end 更大），prev_end 不变
                count += 1
            else:
                # 不重叠：保留当前这个，更新 prev_end
                prev_end = end

        return count