class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        #создаем пустой список из 0 нужной нам длины (езультат должен быть такой же длины, как и входная строка.)
        answer = [0] * n
        
        # Переменная для хранения позиции последнего увиденного 'c'
        # Начинаем с "бесконечности", чтобы в начале были большие расстояния
        pos = -float('inf')
        
        # Первый проход: Слева направо
        for i in range(n):
            if s[i] == c:
                pos = i  #«запоминалка». Она говорит компьютеру: «Я только что увидел нужную нам букву c, запомни, на каком индексе она стоит».
            answer[i] = i - pos
            
        # Второй проход: Справа налево
        pos = float('inf')
        #эти три числа в скобках (start, stop, step)
        for i in range(n - 1, -1, -1):     #This range starts from the last index and moves towards the first one by stepping minus one each time. This allows us to find the closest character on the right side. 
            if s[i] == c:
                pos = i
            # Сравниваем старое расстояние с новым и берем минимум
            answer[i] = min(answer[i], pos - i)
            
        return answer