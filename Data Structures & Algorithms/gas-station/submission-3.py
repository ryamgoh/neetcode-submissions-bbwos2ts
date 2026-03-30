class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue

            print([(x + 1) % n for x in range(i, i + n)])

            j = (i + 1) % n
            while j != i:
                tank += gas[j] - cost[j]
                if tank < 0:
                    break
                j = (j + 1) % n

            if j == i:
                return i
        return -1