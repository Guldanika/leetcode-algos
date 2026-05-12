class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # 1. Если длины разные, это сразу не подходит
        if len(words) != len(s):
            return False
        
        # 2. Проходим по списку слов
        for i, word in enumerate(words):
            # Сравниваем первую букву текущего слова с буквой в s на той же позиции
            if word[0] != s[i]:
                return False
                
        # Если мы прошли весь цикл и не нашли несовпадений
        return True