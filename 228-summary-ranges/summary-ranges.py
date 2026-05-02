class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        s = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                e = nums[i - 1]
                if s == e:
                    ans.append(str(s))
                else:
                    ans.append(str(s) + '->' + str(e))
                if i < len(nums):
                    s = nums[i]

        return ans
            



            #ВТОРОЕ РЕШЕНИЕ 

         #ranges = []     
        #i = 0 
        
        #while i < len(nums): 
        #   start = nums[i]  
        #    while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
        #       i += 1 
            
        #    if start != nums[i]: 
        #        ranges.append(str(start) + "->" + str(nums[i]))
        #    else: 
        #        ranges.append(str(nums[i]))
            
        #    i += 1

        #return ranges



