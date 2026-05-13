class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [0] * n
        
        # Переменная для хранения позиции последнего увиденного 'c'
        # Начинаем с "бесконечности", чтобы в начале были большие расстояния
        pos = -float('inf')
        
        # Первый проход: Слева направо
        for i in range(n):
            if s[i] == c:
                pos = i
            answer[i] = i - pos
            
        # Второй проход: Справа налево
        pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            # Сравниваем старое расстояние с новым и берем минимум
            answer[i] = min(answer[i], pos - i)
            
        return answer