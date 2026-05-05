class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        ans = [''] * len(s)

        for i, c in enumerate(s):
            #Мы перебираем строку s. i — это текущая позиция буквы в #перемешанной строке, а c — сама буква (символ).
            ans[indices[i]] = c
#Метод ''.join(...) берет все элементы из списка ans и склеивает их в одну #строку без разделителей.
        return ''.join(ans)