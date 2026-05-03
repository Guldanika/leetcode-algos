class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # 1. Total number of apples to store
        total_apples = sum(apple)
        
        # 2. Sort capacities from largest to smallest
        capacity.sort(reverse=True)
        
        boxes_used = 0
        
        # 3. Use the biggest boxes first
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            
            # 4. If all apples are in a box, we're done
            if total_apples <= 0:
                break
                
        return boxes_used