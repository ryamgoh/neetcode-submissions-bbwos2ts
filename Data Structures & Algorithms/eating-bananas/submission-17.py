class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum we can eat to hit the h
        # if less, its ok, but we want to maximise such that we do eat totalHour <= h
        # constraints
        # we can only eat a pile at 1 hour
        # once we pick a speed, we stick with speed
        # higher speed = lower totalHour spent eating

        # for piles of [1, 4, 3, 2]
        # if we we choose 4 bananas / h
        # we can finish this within 4 hours
        # but can we do better?
        # YES
        # the slowest we can eat is 1 banana per hour (lowest limit)
        # the fastest we can eat is max of the piles (highest limit)
        # why highest limit? because even if we eat more than the max, we can only eat one pile for each hour, causing a hard maximum

        # in this case, we can use binary search (1, maxPile)
        maxPile = max(piles)

        L = 1
        R = maxPile
        bestSpeed = maxPile # we want to lower this
        while L <= R:
            M = L + (R - L) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / M)
            if total <= h:
                bestSpeed = M
                R = M - 1
            else:
                L = M + 1

        return int(bestSpeed)