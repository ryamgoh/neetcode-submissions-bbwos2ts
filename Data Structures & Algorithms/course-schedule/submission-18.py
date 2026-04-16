class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1

        q = deque()
        for crs in indegree:
            if indegree[crs] == 0:
                q.append(crs)

        res = 0

        while q:
            for _ in range(len(q)):
                crs = q.popleft()
                res += 1
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        return res == numCourses