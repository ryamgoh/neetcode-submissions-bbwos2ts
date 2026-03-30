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

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                    dfs(nei)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count