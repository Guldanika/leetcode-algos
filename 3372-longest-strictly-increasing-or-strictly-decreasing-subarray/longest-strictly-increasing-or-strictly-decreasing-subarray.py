class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        inc = 1
        dec = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                # Strictly increasing
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                # Strictly decreasing
                dec += 1
                inc = 1
            else:
                # Equal values break both streaks
                inc = 1
                dec = 1
            
            max_len = max(max_len, inc, dec)
            
        return max_len

        #To solve this, we need to find the longest continuous streak where the numbers are either strictly going up or strictly going down. Since a single number counts as a subarray of length 1, that will be our baseline.

#Logic
#Initialize: Set max_len, inc_len (increasing), and dec_len (decreasing) to 1.

#Iterate: Loop through the array starting from the second element.

#Check Trends:

#Increasing: If nums[i] > nums[i-1], increment inc_len and reset dec_len to 1.

#Decreasing: If nums[i] < nums[i-1], increment dec_len and reset inc_len to 1.

#Equal: If nums[i] == nums[i-1], both streaks are broken. Reset both inc_len and dec_len to 1.

#Update Global Maximum: After each step, update max_len with the highest value among max_len, inc_len, and dec_len. 
