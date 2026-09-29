import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        # print(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            smashed = max(stone1, stone2) - min(stone1, stone2)
            # print(stone1, stone2, smashed)
            if smashed > 0:
                heapq.heappush_max(stones, smashed)
        if len(stones) > 0:
            return stones[0]
        return 0
        