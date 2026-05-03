class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
    
     # Initialize the two smallest values as infinity
        first_min = second_min = float('inf')
        
        for p in prices:
            if p < first_min:
                # Update both if we find a new absolute minimum
                second_min = first_min
                first_min = p
            elif p < second_min:
                # Update only the second minimum
                second_min = p
        
        min_cost = first_min + second_min
        
        return money - min_cost if min_cost <= money else money