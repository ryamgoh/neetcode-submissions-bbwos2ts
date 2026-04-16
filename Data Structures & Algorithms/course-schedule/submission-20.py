class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        stack = []
        for crs in indegree:
            if indegree[crs] == 0:
                stack.append(crs)

        res = 0

        while stack:
            crs = stack.pop()
            res += 1
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)

        return res == numCourses