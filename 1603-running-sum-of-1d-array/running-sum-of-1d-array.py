class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cumsum = 0
        for num in nums:
            cumsum += num 
            ans.append(cumsum)
        return ans

             