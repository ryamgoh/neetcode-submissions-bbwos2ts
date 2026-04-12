class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]  # we don't care about 0
        rank = [0] * (N + 1)  # we don't care about 0
        
        def find(n):
            if n == par[n]:
                return n
            return find(par[n])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        # O(V + (E * \alpha(V)))