class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Магическая строчка
        return s in (s + s)[1:-1] 

        #[1:-1]  - срезать из конечной выборки первую и последнуюю букву, символ 
        #(s + s) Мы создаем строку в два раза длиннее.
        #This problem has a very clever solution. Instead of using complex loops, we can use a mathematical property. If we double the string and remove the first and last characters, a repeating pattern will still contain the original string in the middle. In Python, this is just a single line of code using string slicing.