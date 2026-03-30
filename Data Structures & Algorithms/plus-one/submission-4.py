class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Start at the least significant digit
        curr_idx = len(digits) - 1
        
        # We need to add 1 to the current digit.
        # Carry should represent the value we are adding to the current position.
        # Initially, we want to add 1.
        carry = 1 
        
        while carry:
            # If we have gone past the start of the list (e.g., 999 + 1 = 1000),
            # we need to insert a new digit at the beginning.
            if curr_idx < 0:
                digits.insert(0, 1)
                break
            
            # Calculate the sum of the current digit and the carry
            total = digits[curr_idx] + carry
            
            # Update the current digit (mod 10 keeps it within 0-9)
            digits[curr_idx] = total % 10
            
            # Update the carry for the next iteration (integer division)
            carry = total // 10
            
            # Move to the next significant digit
            curr_idx -= 1
            
        return digits