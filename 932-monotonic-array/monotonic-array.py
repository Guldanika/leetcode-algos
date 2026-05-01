class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        #def inc(nums):
        #    prev = - float('inf')
         #   for num in nums:
         #       if num < prev:
          #          return False
           #     prev = num 
            #return True 
        
        #def dec(nums):
         #   prev = float ('inf')
          #  for num in nums: 
           #     if num > prev:
            #        return False 
             #   prev = num
            #return True 

        #return inc(nums) or dec(nums)

        inc = True
        dec = True 

        for i in range(1, len(nums)):
            if nums[i] <  nums[i-1]:
                inc = False

            if nums[i] >  nums[i-1]:
                dec = False 

        return inc or dec