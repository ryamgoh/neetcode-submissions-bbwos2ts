import heapq
from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        minCost = []
        currCost = {}
        for i in range(n):
            currCost[i] = 0 if i == src else float("inf")
            heapq.heappush(minCost, (currCost[i], i))

        outDegree = {}
        for u, v, c in edges:
            if u not in outDegree:
                outDegree[u] = []
            outDegree[u].append((v, c))

        not_visited = set(range(n))

        while not_visited:
            # 1. Really extract the current best node
            while minCost:
                val, i = heapq.heappop(minCost)
                if i in not_visited:
                    break
            else:
                break

            # 2. Safe access to neighbours + keep the weight
            for nei, weight in outDegree.get(i, []):
                new_cost = currCost[i] + weight
                if new_cost < currCost[nei]:
                    currCost[nei] = new_cost
                    heapq.heappush(minCost, (new_cost, nei))

            not_visited.remove(i)

        # Convert unreachable nodes if the problem asks for -1
        return {node: (cost if cost != float("inf") else -1)
                for node, cost in currCost.items()}