class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        
        # Растим строку, пока не покроем нужный индекс
        while len(word) < k:
            new_part = ""
            for char in word:
                # ord(char) дает код символа, +1 увеличивает его
                # chr() превращает код обратно в букву
                new_part += chr(ord(char) + 1)
            
            word += new_part
            
        return word[k - 1]
