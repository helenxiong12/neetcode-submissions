class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0: return []
        distances = []
        heapq.heapify(distances)
        for i, (px, py) in enumerate(points):
            dist = px ** 2 + py ** 2
            heapq.heappush(distances, (dist, i))
        # print(distances)
        results = []
        for _ in range(k):
            _, idx = heapq.heappop(distances)
            # print("popped", idx)
            results.append(points[idx])
        return results 
        