class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canFitCapacity(M):
            count = 1
            currSum = 0
            for n in weights:
                if currSum + n > M:
                    count += 1
                    currSum = n
                else: 
                    currSum += n

            if count <= days:
                return True
            return False

        MAX = sum(weights)
        MIN = max(weights)

        best = MAX
        L = MIN
        R = MAX
        while L <= R:
            M = L + (R - L) // 2
            if canFitCapacity(M):
                best = min(best, M)
                R = M - 1
            else:
                L = M + 1
        return best


