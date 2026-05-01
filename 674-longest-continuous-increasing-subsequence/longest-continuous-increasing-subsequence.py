class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0 
        cur = 0 
        prev = -float('inf')

        for num in nums:
            if num > prev:
                cur += 1 
            else:
                cur = 1 

            ans = max(cur, ans)
            prev = num

        return ans
