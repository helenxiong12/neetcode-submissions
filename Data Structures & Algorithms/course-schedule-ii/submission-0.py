class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        
        for p1, p2 in prerequisites:
            graph[p1].append(p2)

        visited = [0] * numCourses
        order = []

        def dfs(course):
            if visited[course] == 2:
                return True
            if visited[course] == 1:
                return False
            visited[course] = 1
            for d in graph[course]:
                if not dfs(d):
                    return False
            order.append(course)
            visited[course] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order