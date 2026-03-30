class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1): # this is impossible
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False # we found a cycle

            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue # we shouldn't need to count the parent since we came from it
                if not dfs(nei, node):
                    return False # we should just return if we detect any downstream

            return True

        return dfs(0, -1) and len(visited) == n