class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Build adjacency list
        adjList = defaultdict(set)
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)
        
        # Find leaves (nodes with degree 1)
        leaves = deque([node for node in range(n) if len(adjList[node]) == 1])
        
        remaining = n
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Remove leaf and update its neighbor
                neighbor = adjList[leaf].pop()
                adjList[neighbor].remove(leaf)
                # If neighbor becomes a leaf, add it to queue
                if len(adjList[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)