class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indg = [0] * numCourses
        adjList = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indg[dst] += 1
            adjList[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indg[n] == 0: # we found one without a prereq
                q.append(n)

        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for nei in adjList[curr]:
                indg[nei] -= 1
                if indg[nei] == 0:
                    q.append(nei)

        return finish == numCourses