class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l,r = 0, len(s) - 1

        while l < r:
            ## Меняем элементы местами
            s[l], s[r] = s[r], s[l]
            ## Двигаем указатели навстречу друг другу
            l += 1
            r -=1
        
     