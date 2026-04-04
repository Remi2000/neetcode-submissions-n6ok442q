"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 时间	O(n log n)	排序占主导，遍历一次是 O(n)
        # 空间	O(1)	原地排序，只用了常数额外空间

        # 按开始时间排序
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            # 后一个的开始时间 < 前一个的结束时间 → 重叠
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True