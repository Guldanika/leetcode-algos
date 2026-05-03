class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        #пытаемся посадить слева
        i = 0 
        while seats[i] == 0:
            i += 1 
        left = i 

        #пытаемся посадить справа 
        i = -1

        while seats[i] == 0:
            i -= 1
        right = -i -1

        #пытаемся посадить посередине
        max_zeros = 0
        cur_zeros = 0

        for s in seats:
            if s == 0:
                cur_zeros += 1
                max_zeros = max(max_zeros, cur_zeros)

            else:
                cur_zeros = 0
                max_zeros = max(max_zeros, cur_zeros)


        mid = (max_zeros +1) // 2

        return max(right, left, mid)

        