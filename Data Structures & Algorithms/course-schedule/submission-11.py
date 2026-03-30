class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegreeMap = {i: 0 for i in range(numCourses)}
        adjList = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            indegreeMap[crs] += 1
            adjList[pre].append(crs)

        q = deque()
        res = []

        for node in indegreeMap:
            if indegreeMap[node] == 0:
                q.append(node)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)
                # get all neighbours:
                for nei in adjList[node]:
                    indegreeMap[nei] -= 1
                    if indegreeMap[nei] == 0:
                        q.append(nei)

        return len(res) == numCourses