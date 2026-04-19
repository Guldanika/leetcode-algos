class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0 
        right = sum(nums)
        ans = []

        for num in nums:
            ans.append(abs(left - (right - num)))

            left += num
            right -= num

        return ans