class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        edge_cnt = {}
        leaves = deque()

        for src, neighbors in adj.items():
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)

        while leaves and n > 2:
            for _ in range(len(leaves)):
                # process node
                node = leaves.popleft()
                n -= 1

                # find neighbours
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        print(edge_cnt)
        return list(leaves)