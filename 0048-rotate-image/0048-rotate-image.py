class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n >> 1):
            for j in range(i, n - 1 - i):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
                matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]        