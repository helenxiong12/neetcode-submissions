class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calculateTime(rate: int) -> int:
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            return time
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if calculateTime(mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        