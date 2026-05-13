class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = 'aeiou' # Набор гласных для проверки
        count = 0 

# Запускаем цикл строго в границах от left до right + 1
        # Мы добавляем +1, так как range в Python не включает последнее число
        for i in range(left, right +1):
            word = words[i]
        # Проверяем первую и последнюю буквы
            if word[0] in vowels and word[-1] in vowels:
                count += 1

        return count