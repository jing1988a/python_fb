# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?



class Solution(object):
    def solveBigBoard(self , locationOfBoard):
        cur=0
        totalLine=self.getTotalLine(locationOfBoard)
        newBoardLocation=self.createNewBoard()# create a new board on disc
        n=10
        while cur<totalLine:
            board=self.getNline(locationOfBoard , totalLine)
            self.writeNewBoardonDisc(newBoardLocation , self.gameOfLife(board))
            cur+=n

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        if not in place , this is simple . just create another matrix and compute the next state for each element

        status with bit
        0=00
        1=01
        2=10
        3=11

        caculate based on neighbors' value & 1 (remove the left bit)

        after caculate all element , loop all element with value>>1

        """
        n=len(board)
        m=len(board[0])
        nextBoard=[[None for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                nextBoard[i][j]=self.getStatus(board , i , j  , m , n)
        return nextBoard

    def nextStatus(board , i , j , m , n):
        totalLife = 0
        for x , y in [[0 ,  -1] , [-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , 1] , [1  , 1] , [1  , 0] , [1 , -1] ]:
            nextI=i+x
            nextJ=j+y
            if 0<=nextI<n and 0<=nextJ<m and board[nextI][nextJ]==1:
                totalLife+=1
        if totalLife==3:
            return 1
        if totalLife>3 or totalLife<2:
            return 0

        if totalLife==2:
            return board[i][j]

