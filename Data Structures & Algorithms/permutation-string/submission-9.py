class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # substring just means contiguous. is s1 = len 3, the substring must be len 3

        if len(s1) > len(s2):
            return False

        window_to_match = {}
        for c in s1:
            window_to_match[c] = window_to_match.get(c, 0) + 1

        window_len = len(s1)
        window = {}
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1 

            if r - l + 1 == window_len:
                if window == window_to_match:
                    return True
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

        return False