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
        # heapq.heapify(rooms)

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            # print(rooms)
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)


        