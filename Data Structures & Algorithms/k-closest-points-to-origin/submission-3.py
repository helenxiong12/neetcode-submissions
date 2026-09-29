class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0: return []
        distances = []
        heapq.heapify(distances)
        for i, (px, py) in enumerate(points):
            dist = px ** 2 + py ** 2
            heapq.heappush(distances, (dist, i))
        # print(distances)
        results = [points[heapq.heappop(distances)[1]] for _ in range(k)]
        return results 
        