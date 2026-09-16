from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # max_k = []
        frequencies = [[] for i in range(len(nums))]

        for key, val in count.items():
            frequencies[val-1].append(key)
        #     if len(max_k) < k:
        #         heapq.heappush(max_k, (val, key))
        #     else: 
        #         heapq.heappushpop(max_k, (val, key))

        # res = list(heapq.nlargest(k, max_k))
        # return [x[1] for x in res]
        res = []
        for i in range(len(nums)-1, -1, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res



        