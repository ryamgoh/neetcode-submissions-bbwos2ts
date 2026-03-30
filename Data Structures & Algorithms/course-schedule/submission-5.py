class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: prerequisite -> list of courses that depend on it
        adjList = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adjList[pre].append(crs)  # pre is prerequisite for crs
            inDegree[crs] += 1
        
        q = deque()
        res = []
        
        # Find courses with no prerequisites
        for node in inDegree:
            if inDegree[node] == 0:
                q.append(node)
        
        # Process in topological order
        while q:
            node = q.popleft()
            res.append(node)
            
            # Use adjacency list instead of iterating through prerequisites
            for dependent in adjList[node]:
                inDegree[dependent] -= 1
                if inDegree[dependent] == 0:
                    q.append(dependent)
        
        return len(res) == numCourses