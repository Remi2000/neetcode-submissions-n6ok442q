"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 时间复杂度 O(nlogn)
        # 空间复杂度 O(n)
        if not intervals:
            return 0

        # 按开始时间排序
        intervals.sort(key=lambda x: x.start)

        # heap 里只存“结束时间”
        heap = []
        # 先放第一个会议的结束时间
        heapq.heappush(heap, intervals[0].end)

        # 从第二个会议开始处理
        for interval in intervals[1:]:
            earliest_end = heap[0]  # 当前最早结束的时间

            if interval.start >= earliest_end:
                # 能复用这个会议室：弹出旧的结束时间，再放新的
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                # 不能复用，需要新会议室
                heapq.heappush(heap, interval.end)

        return len(heap)
