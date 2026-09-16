"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ct = 0
        rooms = []
        heapq.heapify(rooms)

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            # print(rooms)
            start, end = interval.start, interval.end
            if len(rooms) == 0 or rooms[0] > start:
                heapq.heappush(rooms, end)
            else:
                old_end = heapq.heappop(rooms)
                heapq.heappush(rooms, end)
        return len(rooms)


        