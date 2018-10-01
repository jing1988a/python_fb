class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        n=len(matrix)
        if n==0:
            return 
        m=len(matrix[0])
        if m==0:
            return 
        flag1=False
        flag2=False
        for i in range(n):
            if matrix[i][0]==0:
                flag1=True
                break
        for i in range(m):
            if matrix[0][i]==0:
                flag2=True
                break
        for i in range(1 ,  n):
            for j in range(1 , m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1 , n):
            if matrix[i][0]==0:
                for j in range(m):
                    matrix[i][j]=0
        for j in range(1 , m):
            if matrix[0][j]==0:
                for i in range(n):
                    matrix[i][j]=0
        if flag1:
            for i in range(n):
                matrix[i][0]=0
        if flag2:
            for j in range(m):
                matrix[0][j]=0