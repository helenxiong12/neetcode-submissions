"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        end_times = [intervals[0].end]
        heapq.heapify(end_times)

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            most_recent_end = end_times[0]

            if start >= most_recent_end:
                heapq.heapreplace(end_times, end)
            else:
                heapq.heappush(end_times, end)
        return len(end_times)
        
