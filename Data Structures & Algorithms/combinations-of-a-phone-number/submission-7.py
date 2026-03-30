class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        stack = [""]  # Start with empty string
        
        for digit in digits:  # Process each digit sequentially
            current_level = []
            while stack:
                combination = stack.pop()
                # Add each possible character for current digit to existing combinations
                for char in digitToChar[digit]:
                    current_level.append(combination + char)
            # Push all new combinations back to stack for next digit
            stack = current_level
        
        return stack  # stack now contains all valid combinations