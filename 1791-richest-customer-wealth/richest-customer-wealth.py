class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0 

        for a in accounts:
            total = sum(a)
            ans = max(ans,total)

        return ans