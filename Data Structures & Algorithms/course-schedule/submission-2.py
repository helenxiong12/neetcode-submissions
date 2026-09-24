from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. construct a graph
        seen = [0] * numCourses
        def dfs(course):
            if seen[course] == 1:
                return False
            if seen[course] == 2:
                return True
            seen[course] = 1
            for d in courses[course]:
                if not dfs(d):
                    return False # iterate 
            seen[course] = 2
            return True

        courses = defaultdict(set)
        for p1, p2 in prerequisites:
            courses[p2].add(p1) # p1 prereq p2
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        