class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def inc(nums):
            prev = - float('inf')
            for num in nums:
                if num < prev:
                    return False
                prev = num 
            return True 
        
        def dec(nums):
            prev = float ('inf')
            for num in nums: 
                if num > prev:
                    return False 
                prev = num
            return True 

        return inc(nums) or dec(nums)

