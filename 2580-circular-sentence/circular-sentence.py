class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Разрезаем предложение на отдельные слова по пробелам
        words = sentence.split()
        n = len(words)
        
        # 1. Проверяем стыки между соседними словами
        for i in range(n - 1):
            # Последняя буква текущего слова words[i][-1] vs Первая буква следующего words[i+1][0]
            if words[i][-1] != words[i+1][0]:
                return False
        
        # 2. Проверяем "кольцо": последняя буква последнего слова 
        # и первая буква самого первого слова
        if words[-1][-1] != words[0][0]:
            return False
            
        return True