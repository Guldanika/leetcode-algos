class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:       # Пока число не станет однозначным
            new_num = 0      # Сюда будем складывать сумму цифр
            
            while num > 0:   # Разбираем текущее число на части
                num, d = divmod(num, 10)
                new_num += d
            
            num = new_num    # Сумма цифр становится нашим новым числом для проверки
            
        return num

                    
                
