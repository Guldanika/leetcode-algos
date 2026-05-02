class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)   # обновляем минимум
            profit = price - min_price          # считаем прибыль
            ans = max(ans, profit)              # обновляем максимум

        return ans
        