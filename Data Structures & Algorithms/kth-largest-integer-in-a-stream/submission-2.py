import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.k = k
        heapq.heapify(self.queue)
        while len(self.queue) > k:
            heapq.heappop(self.queue)
        # print(self.queue)

    def add(self, val: int) -> int:
        # print(self.queue)
        if len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
        elif val > self.queue[0]:
            heapq.heappushpop(self.queue, val)
        return self.queue[0]
        
        
