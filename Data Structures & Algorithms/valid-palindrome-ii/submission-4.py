class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try deleting the left character OR the right character
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1
        return True