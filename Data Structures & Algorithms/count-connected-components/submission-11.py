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

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1  # Increment count here when we start a new component

        return count