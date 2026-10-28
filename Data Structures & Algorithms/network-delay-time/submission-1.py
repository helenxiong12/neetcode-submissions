import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append((t, v))
        
        minheap = [(0, k)]
        heapq.heapify(minheap)
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0

        while len(minheap) > 0:
            t1, n1 = heapq.heappop(minheap)
            if t1 > dist[n1]:
                continue
            for t2, n2 in graph[n1]:
                if t2 + t1 < dist[n2]:
                    dist[n2] = t2 + t1
                    heapq.heappush(minheap, (dist[n2], n2))
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans


