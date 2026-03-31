class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        L = 0
        window_map = {}
        found = False
        for R in range(len(s2)):
            window_map[s2[R]] = window_map.get(s2[R], 0) + 1
            # Check when window size matches s1 length
            if R - L + 1 == len(s1):
                if count == window_map:
                    return True
                # Then shrink window for next iteration
                window_map[s2[L]] -= 1
                if window_map[s2[L]] == 0:
                    del window_map[s2[L]]
                L += 1
        return False
        