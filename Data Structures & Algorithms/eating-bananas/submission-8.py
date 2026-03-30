class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return min k such that we can eat all bananas within h hours
        # one pile at a time
        # [1, 4, 3, 2]
        # if k = 1,
        # we will take 1 + 4 + 3 + 2 = 10 hours
        # if k = 2,
        # we will take 1 + 2 + 2 +1 = 6 hours
        # we take this because this is the best option that is < h = 9
        # if k = 3,
        # we will take 1 + 2 + 1 + 1 = 5 hours
        best_k = max(piles)

        L = 1
        R = best_k
        while L <= R:
            M = L + (R - L) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / M)

            if time <= h:
                best_k = min(best_k, M)
                R = M - 1
            else:
                L = M + 1

        return best_k