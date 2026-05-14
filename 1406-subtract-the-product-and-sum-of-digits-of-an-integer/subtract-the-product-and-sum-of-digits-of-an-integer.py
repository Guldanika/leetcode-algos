class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0 
        prod = 1

        while n:
            n, d = divmod(n, 10)

            summ += d
            prod *=d
        
        return prod - summ