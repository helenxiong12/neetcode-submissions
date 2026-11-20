from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_freq = [(-v, n) for n, v in counter.items()]
        heapq.heapify(max_freq)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(max_freq)[1])
        return ans