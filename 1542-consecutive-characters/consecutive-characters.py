class Solution:
    def maxPower(self, s: str) -> int:
        
        # If the string has only one character, the power is 1
        if not s:
            return 0
        
        max_power = 1
        current_streak = 1
        
        for i in range(1, len(s)):
            # Check if the current character matches the previous one
            if s[i] == s[i-1]:
                current_streak += 1
            else:
                # Streak broken, update max and reset
                max_power = max(max_power, current_streak)
                current_streak = 1
        
        # Return the larger of the global max or the final streak
        return max(max_power, current_streak)