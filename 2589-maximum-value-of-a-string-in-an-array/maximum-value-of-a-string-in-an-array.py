class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0

        for s in strs:
            # Метод .isdigit() проверяет, состоит ли строка только из цифр
            if s.isdigit():
                current_value = int(s)
            else:
                # Если есть буквы, значением считается длина строки
                current_value = len(s)

# Обновляем максимум, если текущее значение больше
            if current_value > max_val:
                max_val = current_value

        return max_val 