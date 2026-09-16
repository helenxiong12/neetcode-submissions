from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        max_k = []

        for key, val in count.items():
            if len(max_k) < k:
                heapq.heappush(max_k, (val, key))
            else: 
                heapq.heappushpop(max_k, (val, key))

        res = list(heapq.nlargest(k, max_k))
        # print(res)
        return [x[1] for x in res]


        