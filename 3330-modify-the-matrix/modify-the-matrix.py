class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for j in range(cols):  # по столбцам
            # Находим максимум в столбце j
            col_max = max(matrix[i][j] for i in range(rows))
            
            # Заменяем все -1 в столбце j на максимум
            for i in range(rows):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max
        
        return matrix