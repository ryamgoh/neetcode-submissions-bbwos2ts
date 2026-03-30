class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        max_len = 0

        left = 0
        for right in range(len(s)):
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
            c_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len