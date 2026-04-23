class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # intuition:
        # we want the smallest window in s that contains all the characters
        # in t (with the counts, probably using a freq map)
        #
        # once the window has all the required characters (covering t), we can try
        # to shrink it from the left with pointer L to make it as
        # small as possible while still valid

        # we need to store the best window
        bestLen = float("inf")
        best = [-1, -1]

        # build a freq map to store characters in t
        count, window_map = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1

        # have: how many characters currently meet the criteria
        # need: how many distinct characters do we still need? 
        have, need = 0, len(count)

        L = 0 
        for R in range(len(s)):
            if s[R] in count:
                window_map[s[R]] = window_map.get(s[R], 0) + 1
                if window_map[s[R]] == count[s[R]]:
                    have += 1

            while have == need:
                if (R - L + 1) < bestLen:
                    best = [L, R]
                    bestLen = R - L + 1

                if s[L] in count:
                    window_map[s[L]] -= 1
                    if window_map[s[L]] < count[s[L]]:
                        have -= 1
                L += 1
        
        L, R = best
        return s[L:R+1]