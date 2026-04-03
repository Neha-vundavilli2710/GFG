class Solution:
    def diagView(self, mat):   # ✅ renamed
        
        n = len(mat)
        res = []
        
        # Start from first row
        for col in range(n):
            i, j = 0, col
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
        
        # Start from last column
        for row in range(1, n):
            i, j = row, n - 1
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
        
        return res