class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start traversing from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # ONLY return here if we didn't carry over
            
            # If the digit is 9, it becomes 0, and the loop continues
            digits[i] = 0
        
        # If the loop finishes, it means ALL digits were 9 (e.g., [9, 9, 9])
        # So we prepend 1 to the array of zeros (e.g., [1, 0, 0, 0])
        return [1] + digits
    