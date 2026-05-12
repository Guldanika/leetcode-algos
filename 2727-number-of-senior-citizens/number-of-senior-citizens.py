class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        
        for person in details:
            # Извлекаем возраст: он находится на позициях с 11 по 13 (не включая 13)
            # В строке "7868190130M7522" это символы '7' и '5'
            age = int(person[11:13])
            
            if age > 60:
                count += 1
                
        return count

    