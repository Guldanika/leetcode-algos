class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0 
        prod = 1

        while n:
            n, d = divmod(n, 10)
            #divmod берет число n и делит его на 10.

            #d (remainder) — получает остаток. Это всегда будет последняя цифра числа (например, из 123 заберет 3)

            summ += d
            prod *=d

            #Мы берем извлеченную цифру d и добавляем её в наши копилки — прибавляем к сумме и умножаем на неё произведение.
        
        return prod - summ