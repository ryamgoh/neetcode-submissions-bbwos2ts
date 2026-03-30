from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        visited = set()

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(i):
            q = deque([i])
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue # curr is already visited? just ignore. end early
                visited.add(curr) # add to visited set
                for neighbor in adj[curr]:
                    q.append(neighbor)
            
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1  # Increment count here when we start a new component

        return count