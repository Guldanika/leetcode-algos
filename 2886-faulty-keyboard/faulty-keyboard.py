class Solution:
    def finalString(self, s: str) -> str:
      
        ans = ""  # Наш экран ноутбука
        
        for char in s:
            if char == 'i':
                # Если нажали 'i', переворачиваем то, что уже написано
                ans = ans[::-1]
            else:
                # В остальных случаях просто дописываем букву
                ans += char
                
        return ans  


        