class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0 

        for i, c in enumerate(s):
            if c == ' ':
                spaces +=1
            if spaces == k:
                return s[:i]
            
        return s
                
        