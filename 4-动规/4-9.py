class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
        	return 0
        n = len(matrix[0])
        if n == 0:
        	return 0
        M = [([0] * n) for i in range(m)]

        for i in range(m):
        	M[i][0] = matrix[i][0]
        for j in range(1,n):
        	M[0][j] = matrix[0][j]

        for i in range(1,m):
        	for j in range(1,n):
        		if matrix[i][j] == 1:
        			M[i][j] = min(M[i-1][j-1],M[i][j-1],M[i-1][j])+1
        		else:
        			M[i][j] = 0
       	# return max(max(row) for row in M) ** 2
       	return max(max(row) for row in M)
        # return M

# class Solution(object):
#     def maximalSquare(self, matrix):
#         if not matrix or not matrix[0]: return 0
#         M, N, sideLen = len(matrix), len(matrix[0]), [[1 if ch == '1' else 0 for ch in row] for row in matrix]
#         for i in range(1, M):
#             for j in range(1, N):
#                 if matrix[i][j] == '1':
#                     sideLen[i][j] = 1 + min(sideLen[i - 1][j], sideLen[i][j - 1], sideLen[i - 1][j - 1])
#         print sideLen
#         return max(max(row) for row in sideLen) ** 2


s = Solution()
print s.maximalSquare([[1,0,0,1,0],[1,1,1,1,1],[1,0,1,1,1],[1,0,1,0,0]])

